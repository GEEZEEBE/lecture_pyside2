import QtQuick 2.5
import QtQuick.Window 2.2
Window {
   visible: true
   width: 200
   height: 200
   title: qsTr("Hello World")

   Rectangle {
     width: 200
     height: 200
     color: "red"

     Text {
       text: "Hello World"
       anchors.centerIn: parent
     }
   }
}
