import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
Window {
    id: window
    visible: true
    width: 400
    height: 400
    color: "#edfec1"
    title: qsTr("LED On/Off Blink")

    Rectangle {
        height: 200
        color: "#00000000"
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.top: parent.top

        Dial {
            id: dial
            x: 237
            width: 147
            stepSize: 1
            to: 180
            value: 4
            anchors.rightMargin: 16
            anchors.topMargin: 8
            anchors.right: parent.right
            anchors.top: parent.top
            onValueChanged: spinBox.value = dial.value
        }

        SpinBox {
            id: spinBox
            x: 8
            y: 77
            to: 180
            onValueChanged: dial.value = spinBox.value
        }
    }

    Rectangle {
        id: rectangle
        height: 200
        color: "#00000000"
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.left: parent.left

        Button {
            id: button
            x: 40
            y: 27
            text: qsTr("LED On")
        }

        Button {
            id: button1
            x: 247
            y: 27
            text: qsTr("LED Off")
            checked: true
        }

        Text {
            id: text1
            x: 41
            y: 93
            text: qsTr("Status : Dial 20, LED off")
            font.pixelSize: 30
        }
    }
}
