## JSON Message structure

The messages are formed by different keyword. All messages must contain a **command** keyword with a valid command type. The other keywords depend of the command. Check available commands for details.

There are also [some example](#code_example) about how to create the JSON object in different messages

## Available commands

*   [Say](#say_command)
*   [Set](#set_command)
*   [Get](#get_command)
*   [Stop](#stop_command)

### <a id="say_command"></a>Say

Indicates the robot to **say** a sentence. An attitude can be indicated. The following keywords must be indicated:

*   _sentence_: The sentence to be said
*   _attitude_: Attitude to represent. Available attitudes can be retrieved with a [get](#get_command) command

Example:

```json
[{
    "command": "say",
    "sentence": "Hi, my name is Dewey",
    "attitude": "Happy"
}]
```

### <a id="set_command"></a>Set

Command to set different values to the available parameters. Has two keywords: **parameter** and **value**. These are the available parameters:

*   _volume_: The value is a float between 0 and 1 with the new volume
*   _behaviour_: The value is the name of the behaviour to execute
*   _stiffnes_: Value a string with on/off to set (or not) the motor stiffness
*   _language_: The value is a string with the new robot language. Available languages can be retreived with the [get](#get_command) command

Examples:

```json
[{
    "command": "set",
    "parameter": "volume",
    "value": 0.5
}]

[{
    "command": "set",
    "parameter": "behaviour",
    "value": "StandUp"
}]

[{
    "command": "set",
    "parameter": "stiffnes",
    "value": "off"
}]

[{
    "command": "set",
    "parameter": "language",
    "value": "English"
}]
```

### <a id="get_command"></a>Get

Retrieve information from the robot. The information requiered is indicated with the keyword **parameter**. The returned message includes a keyword **"information"** with the data required. The content of the **"information"** keyword depends of the kind of information requested.

*   _volume_: Returns a string with a number between 0 and 1
*   _running_behaviours_: Returns a list of values separated by semicolon ";" with the **running** behaviours
*   _available_behaviours_: Returns a list of values separated by semicolon ";" with the **available** behaviours
*   _available_languages_: Returns a list of values separated by semicolon ";" with the **available** languages
*   _available_attitudes_: Returns a list of values separated by semicolon ";" with the **available** attitudes
*   _battery_: Returns a string representation of the battery level. The battery level is expresed between 0 (empty) and 1 (fully charged)

These examples are the messages received **from** the robot. The message sent is the same without the **information** keyword.

```json
[{
    "command": "get",
    "parameter": "volume",
    "information": "0.5"
}]

[{
    "command": "get",
    "parameter": "running_behaviours",
    "information": "StandUp;Breathing"
}]

  [{
    "command": "get",
    "parameter": "available_behaviours",
    "information": "StandUp;Breathing;Crouch"
}]

[{
    "command": "get",
    "parameter": "available_languages",
    "information": "English;French"
}]

[{
    "command": "get",
    "parameter": "available_attitudes",
    "information": "Happy;Sad;Neutral"
}]
```

### <a id="stop_command"></a>Stop

The **stop** command is sent to stop a specific behaviour or all active behaviours (except the default behaviour, that usually is the server). The only keyword is the **behaviour** that specify what behaviour should be stopped. Use **all** for stopping all the behaviours.

Example:

```json
[{
    "command": "stop",
    "behaviour": "all"
}]
```

## <a id="code_example"></a>Code examples

Here are some examples about how to create messages according to JSON structure

#### Python

```python
# Import JSON module
import json

# The message is a dictionary
message = {}
message['command'] = 'say'
message['sentence'] = 'Hello'
message['attitude'] = 'Happy'

# Just inflate a JSON object with the dictionary
json_message = json.dumps(message)
```

#### Java

```java
JSONObject message = new JSONObject();
try {
    message.put("command", "say");
    message.put("sentence", sentence);
    message.put("attitude", attitude);
} catch (Exception e) {
    e.printStackTrace();
}
```
