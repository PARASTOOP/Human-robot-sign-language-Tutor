<?xml version="1.0" encoding="UTF-8" ?>
<Package name="American Sign language recognition" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="intoduction" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Sign_learn" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Sign_recog" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Play_game" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Finished" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Welldone" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Interactionstart" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="test" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="Excampledialog" src="Excampledialog/Excampledialog.dlg" />
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
    </Dialogs>
    <Resources>
        <File name="prediction" src="prediction.mp3" />
        <File name="Clapping" src="Clapping.mp3" />
        <File name="applause1" src="applause1.wav" />
        <File name="behavior_1" src="behavior_1/behavior_1.pml" />
        <File name="manifest" src="behavior_1/manifest.xml" />
        <File name="swiftswords_ext" src="behavior_1/swiftswords_ext.mp3" />
    </Resources>
    <Topics>
        <Topic name="Excampledialog_enu" src="Excampledialog/Excampledialog_enu.top" topicName="ExampleDialog" language="en_US" nuance="enu" />
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" nuance="enu" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
