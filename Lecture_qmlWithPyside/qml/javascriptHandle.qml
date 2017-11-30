import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import "js/script.js" as MyScript

Window {
    visible: true
    width: 200
    height: 200
    title: qsTr("javascipt Handle")

    Rectangle {
        id: rectangle
        width: 200
        height: 200
        color: "#f3f1a1"
        border.color: "#b7e3fc"

        Button {
            id: button
            x: 45
            y: 29
            text: qsTr("Button")
            font.capitalization: Font.MixedCase
            font.italic: false
            spacing: 0
            enabled: true
            autoExclusive: false
            checked: false
            autoRepeat: false
            checkable: true
            highlighted: true
        }
    }

    Connections {
        target: button
        onClicked: MyScript.jsFunction()
    }

}

