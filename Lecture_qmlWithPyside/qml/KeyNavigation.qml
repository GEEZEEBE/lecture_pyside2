import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Controls 2.2

Window {
    visible: true
    width: 200
    height: 200
    title: qsTr("Key Navigation")

    Rectangle {
        width: 200
        height: 200
        color: "#fcfcac"
        Keys.onLeftPressed: image.rotation = (image.rotation - 10) % 360
        Keys.onRightPressed: image.rotation = (image.rotation + 10) % 360
        focus: true
     Image {
         id: image
         x: 50
         y: 50
         width: 100
         height: 100
         source: "images/tree.png"
     }
   }
}
