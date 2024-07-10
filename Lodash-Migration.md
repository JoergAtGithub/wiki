# Migrate from Lodash to ES6/ES7 features

Starting from Mixxx 2.5.0, the embedded `lodash.mixxx.js` library is deprecated and planned for removal in Mixxx 2.6.0. 
This document is here to help controller maintainers migrate from Lodash functions to ES6/ES7 new features.

## `_.assign`

`_.assign` can simply be replaced by `Object.assign`.

## `_.merge`

`_.merge` works like `_.assign` except it recursively merge two objects. Such a use case is currently unknown in Mixxx controllers. 
However, if you have a valid use case for `_.merge`, don't hesitate to [open an issue](https://github.com/mixxxdj/mixxx/issues) 
describing it.

## `_.forEach`

`_.forEach` can transparantly be replaced by `Array.prototype.forEach` when using an `Array`, a `Map` and other common 
containers and [`for … of`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/for...of) 
for most of other Js iterables.

A key/value pair iteration over objects is also achivable using `Object.entries` and `Map.prototype.entries`:

```js
const opts = {
   var1 : "Test",
}

Object.entries(opts).forEach(([k, v]) => {
  // do something here
});

const map = new Map([
  [1, "un"],
  [2, "deux"],
  [3, "trois"],
]);

map.forEach((k, v) => {
  // do something here
});
```

## `_.map`

For `Array`'s, `_.map`can transparently be replaced by `Array.prototype.map` in most cases:

```js
[1, 2, 3].map(it => it + 1);
```


## `_.filter`

`_.filter` can be replaced by `Array.prototype.filter` for `Array` and `Object.entries(obj).filter`:

```js
[1, 2, 3, 4, 5].filter(it => it % 2 === 0);

Object.entries({
  midi: [], deckNum: 1
}).filter(
  ([k, v]) => Number.isInteger(v)
);
```

# Sparse Arrays

When instanciating an `Array`, using the constructor, `_.map`, `_.filter` and `_.forEach` work differently
than their `Array.prototype` counterparts on [sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays).

```js
let arr = Array(4);
// [ <4 empty items> ]
_.map(arr, (_elem, i) => i);
// [ 0, 1, 2, 3 ]
arr.map((_elem, i) => i)
// [ <4 empty items> ]
```

In most cases, it's better to instanciate and initialize the `Array` in the same expression using `[]`.
In particularly large arrays, you can use the fact that `Array.prototype.fill` does not ignore empty items
to initalize the array with some value and then iterate over that (eg `Array(16).fill(0).map(...)`).

# Other?

The function above are the one typically used in official controllers. If you have another usecase, 
don't hesitate to open an issue so we can documnent it here.