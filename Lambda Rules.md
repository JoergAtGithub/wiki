# Rules and arrangements using lambdas scheme for database access

  - Beware of recursive lambda calls.
  - All database access must be applied in separate thread
    (`TrackCollections` thread). So all database access must be wrapped
    into lambda (via `m_pTrackCollection->callAsync/callSync`).

<!-- end list -->

  - It is strictly prohibited to access GUI from lambda. GUI access must
    be be applied only from main thread.

<!-- end list -->

  - If you need to access GUI from lambda it can be done by emitting
    signal (`ConnectionType` must be `Qt::QueuedConnection`.
  - All access to GUI moves to separate private slot (`slotChangeUI`).
  - Signal must be created (`changeUI`).
  - `changeUI` connects to `slotChangeUI` with last parameter
    `Qt::QueuedConnection`.
  - **OR** You can use helper class `MainExecuter`, which is constructed
    like `TrackCollection` and has its methods `callSync/callAsync`.
    Using `MainExecuter` you must wrap UI access to lambda.

-----

**Example.**

Please, take a look at `DlgMissing::onShow()`. Here we must disable
button after calling `m_pMissingTableModel->select();`

So we created: `private slots: void slotActivateButtons(bool enable);`

connect it: `connect(this, SIGNAL(activateButtons(bool)), this,
SLOT(slotActivateButtons(bool)), Qt::QueuedConnection);`

and call it from the lambda inside `DlgMissing::onShow()`:

``` 
    // tro's lambda idea
    m_pTrackCollection->callAsync(
                [this] (void) {
        m_pMissingTableModel->select();
        // no buttons can be selected
        emit(activateButtons(false));
    });
```
