#Persistent
#NoEnv
SetBatchLines, -1
ListLines, Off
SetTimer, WatchActiveWindow, 100
CoordMode, Mouse, Screen
CoordMode, ToolTip, Screen

lastWindowID := ""
lastMousePositions := {}

WatchActiveWindow:
    WinGet, currentID, ID, A
    if (currentID != lastWindowID) {
        if (lastWindowID) {
            MouseGetPos, lastX, lastY
            lastMousePositions[lastWindowID] := [lastX, lastY]
        }

        if lastMousePositions.HasKey(currentID) {
            coords := lastMousePositions[currentID]
            MouseMove, coords[1], coords[2], 0  ; 0 = instant move
        } else {
            ; Ako nema zapamćenu poziciju, postavi na centar prozora
            WinGetPos, X, Y, W, H, ahk_id %currentID%
            centerX := X + (W // 2)
            centerY := Y + (H // 2)
            MouseMove, centerX, centerY, 0
        }

        lastWindowID := currentID
    }
return
