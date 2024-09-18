Since C++17 an if statement with extra initalizer is supported.
* https://en.cppreference.com/w/cpp/language/if
* https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0305r0.html

This helps to keep the scope of local variables inside the conditional block. 
This may come with a cost of obscuring the clarity of the logic, by moving the actual condition to the right.  

Since this is a new technique not yet used in the Mixxx code base this page shall help to cosider where it is benefical to use it and where it makes the code harder to read. 

### Locking scopes

The case wehere a narrow scope is mandantory is this: 
```cpp
{ // Locking scope
    std::lock_guard shared_flag_lock(mx)
    if (shared_flag)
    {
        unsafe_ping();
        shared_flag = false;
    }
}
```
it can become: 
```cpp
if (std::lock_guard shared_flag_lock(mx); shared_flag)
{
    unsafe_ping();
    shared_flag = false;
}
```

The later reduces netsting, but the informative extra locking scope is no longer obvious. It is not instantly clear that the return value of `shared_flag_lock(mx)` is not checked. 

### Error checking 

We have for example this case: 
https://github.com/mixxxdj/mixxx/blob/6b4a6f9bfd28a553e390d996662f840747c5d782/src/encoder/encoderwave.cpp#L171

```cpp
    int ret;
    if (!m_metaDataTitle.isEmpty()) {
        ret = sf_set_string(m_pSndfile, SF_STR_TITLE, m_metaDataTitle.toUtf8().constData());
        if (ret != 0) {
            qWarning("libsndfile error: %s", sf_error_number(ret));
        }
    }
```

which may make use of the if with initalizer like this
```cpp
    if (!m_metaDataTitle.isEmpty()) {
        if (int ret = sf_set_string(m_pSndfile, SF_STR_TITLE, m_metaDataTitle.toUtf8().constData()); ret != 0) {
            qWarning("libsndfile error: %s", sf_error_number(ret));
        }
    }
```

The later narrows the scope of the POD `ret`, but with no mandatory needs. This comes with the cost of inverted read order. 
In the original code, the reviewers reads the code in the execution order. They will be able to qickly reqognice that the conditional block as unlikely error path. In the new code, the exceptionl error checking code path is focussed, instead of the original step of setting the string.  

This is the code after applying clang-format changes 
```cpp
    if (int ret = sf_set_string(m_pSndfile,
                SF_STR_TITLE,
                m_metaDataTitle.toUtf8().constData());
            ret != 0) {
        qWarning("libsndfile error: %s", sf_error_number(ret));
    }
```

### Getter

here we have this case: 
https://github.com/mixxxdj/mixxx/blob/6b4a6f9bfd28a553e390d996662f840747c5d782/src/encoder/encoderfdkaacsettings.cpp#L51

```cpp
int EncoderFdkAacSettings::getQualityIndex() const {
    int qualityIndex = m_pConfig->getValue(
            ConfigKey(RECORDING_PREF_KEY, kQualityKey), kDefaultQualityIndex);
    if (qualityIndex >= 0 && qualityIndex < m_qualList.size()) {
        return qualityIndex;
    } else {
        kLogger.warning()
                << "Invalid qualityIndex:"
                << qualityIndex << "(Max is:" << m_qualList.size() << "). Ignoring it"
                << "and returning default, which is:" << kDefaultQualityIndex;
    }
    return kDefaultQualityIndex;
}
```

this may become 

```cpp
int EncoderFdkAacSettings::getQualityIndex() const {
    if (int qualityIndex = m_pConfig->getValue(
                ConfigKey(RECORDING_PREF_KEY, kQualityKey), 
                kDefaultQualityIndex);
            qualityIndex >= 0 && qualityIndex < m_qualList.size()) {
        return qualityIndex;
    } else {
        kLogger.warning()
                << "Invalid qualityIndex:"
                << qualityIndex << "(Max is:" << m_qualList.size() << "). Ignoring it"
                << "and returning default, which is:" << kDefaultQualityIndex;
    }
    return kDefaultQualityIndex;
}
```

The later narrows the scope of the POD `qualityIndex`, but still with no mandatory needs. 
Even though the coditional block ist the likely code path, we see the inversion of execution order when reading. 


### Asignment within the consition 

```cpp
    if (Color color = color.getColor()) {
        qDebug() << "The color is:" color:  
        return color; 
    }
```

This is considered as confusing by some developers. We may write it as: 

```cpp
    Color color = color.getColor()
    if (color) {
        qDebug() << "The color is:" color:  
        return color; 
    }
```

With the new syntax we are abel to make it explicite and probabyl less confusing: 
```cpp
    if (Color color = color.getColor(); color) {
        qDebug() << "The color is:" color:  
        return color; 
    }
```

The later has a clear benefit if color is a heavy object and the function is long. There is not really an issue with reading since the condition is simple and the line don't require a line break. 


## Related

### C++ Core Guidelines 

https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#es5-keep-scopes-small

> Flag when expensive resources, such as file handles and locks are not used for N-lines (for some suitable N)

https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#es87-dont-add-redundant--or--to-conditions

> This rule is especially useful when a declaration is used as a condition

```cpp
if (auto pc = dynamic_cast<Circle*>(ps)) { ... } // execute if ps points to a kind of Circle, good

if (auto pc = dynamic_cast<Circle*>(ps); pc != nullptr) { ... } // not recommended 
``` 

### clang-tidy rules 

There is a clang-tidy rule that considers this style as bugprone: 
https://clang.llvm.org/extra/clang-tidy/checks/bugprone/assignment-in-if-condition.html

### stackoverflow

https://stackoverflow.com/questions/17681535/when-would-you-want-to-assign-a-variable-in-an-if-condition
 
