#Persistent
SetTimer, FollowActiveWindow, 100
return

FollowActiveWindow:
    WinGet, winID, ID, A
    if (winID != prevWinID)
    {
        prevWinID := winID
        WinGetPos, X, Y, W, H, ahk_id %winID%
        CenterX := X + (W // 2)
        CenterY := Y + (H // 2)
        DllCall("SetCursorPos", "int", CenterX, "int", CenterY)
    }
return

