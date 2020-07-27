## Adding a revision
- Add a new revision to `res/schema.xml`, which is parsed by `src/database/schemamanager`
  - Increment the `version` attribute by one from the previous one
  - Use the `min_compatible` version from the previous revision unless you delete or rename a table or column
- Summarize your changes in the `description` subtag for future reference
- Add [SQLite](https://www.sqlite.org) statements in the `sql` subtag

## Using the revision
- Update `MixxxDB::kRequiredVersion` in `src/database/mixxxdb.cpp` to the new version
- Add tests to make sure your additions function as expected :)

Note that, once a revision is upgraded to, changes to it won't be recognized - so if you want to fix something afterwards you either have to change the version a few times or always work with a fresh database. Thus, once a revision is in master, it may not be modified bar extraordinary circumstances.