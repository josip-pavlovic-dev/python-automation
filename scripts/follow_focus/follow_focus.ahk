#Persistent
#NoEnv
SetBatchLines, -1
ListLines, Off
SetTimer, WatchActiveWindow, 100
CoordMode, Mouse, Screen
CoordMode, ToolTip, Screen

; ================== PODESAVANJE ==================
LaunchGuardMs := 1500     ; koliko dugo posle klika “cuvamo” kursor (1200–1800ms je realno)
MaxJumpPx     := 120      ; max dozvoljeno pomeranje tokom guarda (0 = potpuni freeze)
; =================================================

global LaunchGuard := false
global LastClickX := 0, LastClickY := 0, LastClickTick := 0

lastWindowID := ""
lastMousePositions := {}

; --- Aktivira guard na levi klik (po zelji i desni) ---
~LButton::
    MouseGetPos, LastClickX, LastClickY
    LastClickTick := A_TickCount
    LaunchGuard := true
    SetTimer, __ClearLaunchGuard, -%LaunchGuardMs%
return

~RButton::
    MouseGetPos, LastClickX, LastClickY
    LastClickTick := A_TickCount
    LaunchGuard := true
    SetTimer, __ClearLaunchGuard, -%LaunchGuardMs%
return

__ClearLaunchGuard:
    LaunchGuard := false
return

; --- Bezbedno pomeranje misa (limitirano tokom guarda) ---
SafeMouseMove(xTarget, yTarget, speed := 0) {
    global LaunchGuard, LastClickX, LastClickY, MaxJumpPx
    if (!LaunchGuard) {
        MouseMove, xTarget, yTarget, speed
        return
    }
    ; Ako je guard aktivan, ogranicimo skok
    if (MaxJumpPx <= 0) {
        ; totalni freeze tokom guarda
        return
    }
    dx := xTarget - LastClickX
    dy := yTarget - LastClickY
    dist := Sqrt(dx*dx + dy*dy)
    if (dist <= MaxJumpPx) {
        MouseMove, xTarget, yTarget, speed
    } else {
        scale := MaxJumpPx / dist
        xClamped := LastClickX + dx * scale
        yClamped := LastClickY + dy * scale
        MouseMove, xClamped, yClamped, speed
    }
}

WatchActiveWindow:
    WinGet, currentID, ID, A
    if (currentID != lastWindowID) {
        if (lastWindowID) {
            ; zapamti poslednju poziciju misa za prethodni prozor
            MouseGetPos, lastX, lastY
            lastMousePositions[lastWindowID] := [lastX, lastY]
        }

        ; na promenu prozora: vrati kursor na poslednju poziciju tog prozora (ili centar),
        ; ali koristi SafeMouseMove da ostane blizu mesta klika dok traje LaunchGuard
        if lastMousePositions.HasKey(currentID) {
            coords := lastMousePositions[currentID]
            SafeMouseMove(coords[1], coords[2], 0)
        } else {
            WinGetPos, X, Y, W, H, ahk_id %currentID%
            centerX := X + (W // 2)
            centerY := Y + (H // 2)
            SafeMouseMove(centerX, centerY, 0)
        }

        lastWindowID := currentID
    }
return

