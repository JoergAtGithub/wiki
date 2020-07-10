```
                           Controller
           MidiController              HidController BulkController
PortMidiController Hss1394Controller
```


```
                  ControllerMappingProcessor
ModularControllerMappingProcessor   LegacyControllerMappingProcessor
                           LegacyMidiControllerMappingProcessor

                                   Controller
              MidiController  HidController  BulkController
PortMidiController Hss1394Controller

                      ScriptEngine
                ControllerScriptEngine
ModularControllerScriptEngine LegacyControllerScriptEngine

```