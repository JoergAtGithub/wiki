# MixxxScript Documentation

## API Documentation

To be written...

## Example Scripts

#### Auto-Crossfader

var button = QPushButton();

function doFade() {

``` 
   var time = 4000;
```

``` 
   var s = Mixxx.getValue("[[Master]]", "crossfader");
   var e = -1.0;
```

``` 
   if (s < 0.0) {
       e = 1.0;
   }
```

``` 
   Mixxx.startFade("[[Master]]", "crossfader");
   Mixxx.point(0, s);
   Mixxx.point(time, e);
   Mixxx.endFade();
```

}

button.text = "Crossfade"; button.clicked.connect(doFade);
button.show();
