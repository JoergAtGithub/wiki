### warning: 'QString::operator const char\*() const' is deprecated

You'll see this any time there's an implicit or explicit cast from a
QString to a character array. To correct it, use the following example:

    QString originalString = "blah";
    QByteArray charableString = QString(originalString).toUtf8();

Then use `charableString` where the original string was used and all
should be well.
