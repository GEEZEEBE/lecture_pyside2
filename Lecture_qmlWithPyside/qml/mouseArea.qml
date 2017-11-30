import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Controls 2.2

Window {
    id: window
    visible: true
    width: 200
    height: 200
    title: "MouseArea"

    Rectangle {
        id: rectangle
        color: mouseArea.containsMouse ? "green" : "black"
        anchors.rightMargin: 20
        anchors.leftMargin: 20
        anchors.bottomMargin: 20
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.topMargin: 20


        MouseArea {
            id: mouseArea
            hoverEnabled: true
            anchors.fill: parent
            onPressed: parent.color = "green"
            onReleased: parent.color = "black"
        }
    }
}
