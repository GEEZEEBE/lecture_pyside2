import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
Window {
   visible: true
   width: 300
   height: 200
   title: qsTr("LED On/Off Blink")

   Rectangle {
       width: 300
       height: 200
       color: "#f8cea3"

       Button {
           id: button
           x: 18
           y: 38
           text: qsTr("LED On")
       }

       Button {
           id: button1
           x: 174
           y: 38
           text: qsTr("LED Off")
       }

       Text {
           id: text1
           x: 42
           y: 118
           text: qsTr("LED Status : Off")
           z: 0
           style: Text.Normal
           font.pixelSize: 30
       }
   }
}
