import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Layouts 1.3
Window {
    visible: true
    width: 400
    height: 400
    title: qsTr("Positioner")

   Grid {
       id: grid
       x: 10
       y: 10
       width: 200
       height: 200
       spacing: 5
       rows: 5
       columns: 5

       Repeater {
           model: 23

           Rectangle {
               id: rectangle
               width: 30
               height: 30
               color: "#e6fdc2"

               Text {
                   id: text1
                   text: index
                   horizontalAlignment: Text.AlignHCenter
                   verticalAlignment: Text.AlignVCenter
                   wrapMode: Text.WordWrap
                   font.pixelSize: 12
               }
           }

       }
   }
}
