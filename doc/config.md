### Config: Basic

These values are mostly passed to [pywm](https://github.com/jbuchermn/pywm) and configure basic behaviour needed c-side.

| Configuration key                    | Default value | Description                                                                                             |
| ------------------------------------ | ------------- | --------------------------------------------------------------------------------------------------------|
| `outputs`                            |               | List of dictionaries: Output configuration (see next lines)                                             |
| `output.name`                        | `""`          | String: Name of output to attach config to actual output                                                |
| `output.scale`                       | `1.0`         | Number: HiDPI scale of output                                                                           |
| `output.width`                       | `0`           | Integer: Output width (or zero to use preferred)                                                        |
| `output.height`                      | `0`           | Integer: Output height (or zero to use preferred)                                                       |
| `output.mHz`                         | `0`           | Integer: Output refresh rate in milli Hertz (or zero to use preferred)                                  |
| `output.pos_x`                       | `None`        | Integer: Output position x in layout (or None to be placed automatically)                               |
| `output.pos_y`                       | `None`        | Integer: Output position y in layout (or None to be placed automatically)                               |
| `output.anim`                        | `True`        | Bool: Enable or disable most animations on this output (useful for virtual outputs)                     |
| `output.transform`                   | `0`           | Integer: Rotation of the screen (see Config: Transform below this section)                              |
| `output.background.path`             |               | String: Optionally specify wallpaper for this output (overrides `background.path`)                      |
| `output.background.anim`             | `True`        | Bool: Optionally disable movements of the background (overrides `output.anim` and `background.anim`)    |
| `pywm`                               |               | Dictionary: [pywm](https://github.com/jbuchermn/pywm) config, see possible keys below                   |
| `pywm.enable_xwayland`               | `False`       | Boolean: Start `XWayland`                                                                               |
| `pywm.xkb_model`                     |               | String: Keyboard model (`xkb`)                                                                          |
| `pywm.xkb_layout`                    |               | String: Keyboard layout (`xkb`)                                                                         |
| `pywm.xkb_variant`                   |               | String: Keyboard variant (`xkb`)                                                                        |
| `pywm.xkb_options`                   |               | String: Keyboard options (`xkb`)                                                                        |
| `pywm.outputs`                       |               | List of dicts: Output configuration (see next lines)                                                    |
| `pywm.output.name`                   | `""`          | String: Name of output to attach config to actual output                                                |
| `pywm.output.scale`                  | `1.0`         | Number: HiDPI scale of output                                                                           |
| `pywm.output.width`                  | `0`           | Integer: Output width (or zero to use preferred)                                                        |
| `pywm.output.height`                 | `0`           | Integer: Output height (or zero to use preferred)                                                       |
| `pywm.output.mHz`                    | `0`           | Integer: Output refresh rate in milli Hertz (or zero to use preferred)                                  |
| `pywm.output.pos_x`                  | `None`        | Integer: Output position x in layout (or None to be placed automatically)                               |
| `pywm.output.pos_y`                  | `None`        | Integer: Output position y in layout (or None to be placed automatically)                               |
| `pywm.xcursor_theme`                 |               | String: `XCursor` theme (if not set, read from; if set, exported to `XCURSOR_THEME`)                    |
| `pywm.xcursor_size`                  | `24`          | Integer: `XCursor` size (if not set, read from; if set, exported to `XCURSOR_SIZE`)                     |
| `pywm.tap_to_click`                  | `True`        | Boolean: On touchpads use tap for click enter                                                           |
| `pywm.natural_scroll`                | `True`        | Boolean: On touchpads use natural scrolling enter                                                       |
| `pywm.focus_follows_mouse`           | `True`        | Boolean: `Focus` window upon mouse enter                                                                |
| `pywm.contstrain_popups_to_toplevel` | `False`       | Boolean: Try to keep popups contrained within their window                                              |
| `pywm.encourage_csd`                 | `True`        | Boolean: Encourage clients to show client-side-decorations (see `wlr_server_decoration_manager`)        |
| `pywm.debug`                         | `False`       | Boolean: Loglevel debug plus output debug information to stdout on every F1 press                       |
| `pywm.texture_shaders`               | `basic`       | String: Shaders to use for texture rendering (see `src/wm/shaders/texture`)                             |
| `pywm.renderer_mode`                 | `pywm`        | String: Renderer mode, `pywm` (enable pywm renderer, and therefore blur), `wlr` (disable pywm renderer) |

### Config: Transform

If you want to rotate an output you can use pywm globals. In your `config.py` import them by adding these lines :

```python
from pywm import {
    PYWM_TRANSFORM_90,
    PYWM_TRANSFORM_180,
    PYWM_TRANSFORM_270,
    PYWM_TRANSFORM_FLIPPED,
    PYWM_TRANSFORM_FLIPPED_90,
    PYWM_TRANSFORM_FLIPPED_180,
    PYWM_TRANSFORM_FLIPPED_270,
}
```

You can then use them by adding this line to your output config :

```python
"transform": PYWM_TRANSFORM_FLIPPED_90,
```

### Config: General appearance

Some basic appearence and animation related configuration:

| Configuration key               | Default value | Description                                                                                                                                                                        |
| ------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `background.path`               |               | String: Path to background image (replaces obsolete `wallpaper`)                                                                                                                   |
| `background.time_scale`         | `0.15`        | Number: Time scale of background movement                                                                                                                                          |
| `background.anim`               | `True`        | Bool: Prevent (`False`) background movement                                                                                                                                        |
| `blend_time`                    | `1.0`         | Number: Time in seconds to blend in and out (at startup and shutdown)                                                                                                              |
| `anim_time`                     | `.3`          | Number: Timescale of all animations in seconds                                                                                                                                     |
| `corner_radius`                 | `18`          | Number: Radius of blacked out corners of display (0 to disable)                                                                                                                    |
| `view.corner_radius`            | `12`          | Number: Corner radius of views (0 to disable)                                                                                                                                      |
| `view.padding`                  | `6`           | Number: Padding around windows in normal mode (pixels)                                                                                                                             |
| `view.fullscreen_padding`       | `0`           | Number: Padding around windows when they are in fullscreen (pixels)                                                                                                                |
| `interpolation.size_adjustment` | `.5`          | Number: When window size adjustments of windows (slow) happen during gestures and animations, let them take place at the middle (`.5`) or closer to start / end (`.1` / `.9` e.g.) |

A very basic server-side decoration implementation is available (unicolor rounded corners border around a view). This will be displayed on views requesting SSDs and floating views.

| Configuration key               | Default value | Description                            |
| ------------------------------- | ------------- | -------------------------------------- |
|`view.ssd.enabled`               |`True`         | Enable SSD drawing                     |
|`view.ssd.color`                 |`'#BEBEBEFF'`  | Color of the border                    |
|`view.ssd.width`                 |`2`            | Width in pixels                        |

Also a border highlight can be displayed around focused windows:

| Configuration key               | Default value | Description                            |
| ------------------------------- | ------------- | -------------------------------------- |
|`focus.enabled`                  |`True`         | Enable the fous highlight              |
|`focus.color`                    |`'#19CEEB55'`  | Color of the focus highlight           |
|`focus.distance`                 |`4`            | Width of the border                    |
|`focus.width`                    |`2`            | Distance to view                       |
|`focus.animate_on_change`        |`False`        | Show an animation when focus changes   |
|`focus.anim_time`                |`0.3`          | Timescale of this animation            |

### Config: Behaviour, keys and gestures

The most important configuration options with regard to behaviour are `mod` and `key_bindings`; see below for them and some more detailed ones.

| Configuration key        | Default value         | Description                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key_bindings`           | `lambda layout: []`   | Key bindings as array, see `default_config.py`, `layout.py` and [dotfiles](https://github.com/jbuchermn/dotfiles/blob/master/newm/home/.config/newm/config.py))                                                                                                                                                                           |
| `view.send_fullscreen`   | `True`                | Let clients know when they are set to fullscreen (which leads to them adjusting, e.g. YouTube fullscreen)                                                                                                                                                                                                                                 |
| `view.accept_fullscreen` | `True`                | Set a view to fullscreen, if it requests so, setting this to `False` will leave a view in its tile while the view thinks it is in fullscreen mode, which might be desirable                                                                                                                                                               |
| `view.floating_min_size` | `True`                | Try to open floating views in their minimal size instead of their preferred one. This doesn't always work as not all view report minimal size                                                                                                                                                                                             |
| `view.border_ws_switch`  | `10.`                 | Amount of pixels a view, which is currently being moved, has to reach into a new output to be switched over to this new output                                                                                                                                                                                                            |
| `view.rules`             | `lambda view: None`   | Function: Set rules based on a view (e.g. based on `view.app_id`): Return a dict with all rules set (see below for possible rules).                                                                                                                                                                                                       |
| `lock_on_wakeup`         | `True`                | Lock screen after wake up is detected (does not work as well as locking on systemd sleep)                                                                                                                                                                                                                                                 |
| `greeter_user`           | `'greeter'`           | Relevant if newm is run as login display manager, username used for `greetd`                                                                                                                                                                                                                                                              |
| `on_startup`             | `lambda: None`        | Function called when the compositor has started, use to run certain things using `os.system("... &")`                                                                                                                                                                                                                                     |
| `on_reconfigure`         | `lambda: None`        | Function called when the compositor has reloaded the config                                                                                                                                                                                                                                                                               |
| `synchronous_update`     | `lambda: None`        | Function: called once per frame, can be used to e.g. update backlight dynamically. Be careful, will block the compositor.                                                                                                                                                                                                                 |
| `view.debug_scaling`     | `False`               | Debug sclaing of views - if you think views look blurry, this outputs potential issues where logical size and size on the display do not match                                                                                                                                                                                            |
| `enable_unlock_command`  | `True`                | Boolean: Enable `newm-cmd unlock` to unlock the compositor from second tty if lock screen breaks.                                                                                                                                                                                                                                         |
| `energy.idle_callback`   | `lambda event: None`  | Callback called with events `"lock", "idle", "idle-lock", "idle-presuspend", "idle-suspend", "active", "sleep", "wakeup"` to e.g. adjust backlight. See [layout.py](https://github.com/jbuchermn/newm/blob/master/newm/layout.py) and [default_config.py](https://github.com/jbuchermn/newm/blob/master/newm/default_config.py)           |
| `energy.idle_times`      | `[120, 300, 600]`     | Times to dim, lock and suspend, empty list disables energy management.                                                                                                                                                                                                                                                                    |
| `energy.suspend_command` | `"systemctl suspend"` | Command called to suspend after `power_times[2] has passed`.                                                                                                                                                                                                                                                                              |

The following rules can be used in `view.rules`:
- `opacity` (e.g. `lambda view: {'opacity': 0.8 }`): Set transparency of view.
- `blur` (e.g. `lambda view: { 'blur': { 'raidus': 5, passes: 2 }}`): Apply background Kawase blur with radius and passes.
- `float`, `float_size` (oprional) and `float_pos` (optional), e.g. `lambda view: { 'float': True, 'float_size': (300, 300), 'float_pos': (0.5, 0.5)}`: Always open certain views floating, possibly supplying size and position.

Gesture bindings can be configured, where the first entry in the tuple describes a modifier (e.g. "L", the gesture will only be detected if Logo is held down meanwhile). The examples below are exhaustive for 1-5 finger gestures which can be used:

| Configuration key                      | Default value                          | Description                                                                       |
| -------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------- |
|`gesture_bindings.launcher`             |`(None, "swipe-5")`                     | Binding which slides in the launcher panel                                        |
|`gesture_bindings.move_resize`          |`("L", "move-1", "swipe-2")`            | Bindings for moving (second in tuple) and resizing (third in tuple) a view        |
|`gesture_bindings.swipe`                |`(None, "swipe-3")`                     | Binding to swipe between tiles                                                    |
|`gesture_bindings.swipe_to_zoom`        |`(None, "swipe-4")`                     | Binding to zoom in and out                                                        |

Gesture sensitivity and the like are configured by a lot of numeric parameters; these are structured by the different gesture kinds (swipe to move, swipe to zoom, move, resize)
as well as some general ones (`gestures` and `grid`). The best way is to experiment with these and hot-reload the configuration (by default `M-C`). Also `grid.py` acts as a
plot script when (`grid.debug`) is enabled.

| Configuration key              | Default value |
| ------------------------------ | ------------- |
| `gestures.lp_freq`             | `60.`         |
| `gestures.lp_inertia`          | `.8`          |
| `gestures.two_finger_min_dist` | `.1`          |
| `gestures.validate_threshold`  | `.02`         |
| `grid.debug`                   | `False`       |
| `grid.min_dist`                | `.05`         |
| `grid.throw_ps`                | `[1, 5, 15]`  |
| `grid.time_scale`              | `.3`          |
| `resize.grid_m`                | `3`           |
| `resize.grid_ovr`              | `0.1`         |
| `resize.hyst`                  | `0.2`         |
| `swipe.gesture_factor`         | `4`           |
| `swipe.grid_m`                 | `1`           |
| `swipe.grid_ovr`               | `0.2`         |
| `swipe.lock_dist`              | `0.01`        |
| `swipe_zoom.gesture_factor`    | `4`           |
| `swipe_zoom.grid_m`            | `1`           |
| `swipe_zoom.grid_ovr`          | `0.2`         |
| `swipe_zoom.hyst`              | `0.2`         |
| `move.grid_m`                  | `3`           |
| `move.grid_ovr`                | `0.2`         |
| `move_resize.gesture_factor`   | `2`           |

Configurable actions on keybindings can be any function calls on `layout`. Check the class `Layout` and [layout](layout.md) for details.

### Config: Gesture providers

Gestures can stem from various sources, most importantly from wlroots and libinput (referred to as *c gestures*), from evdev directly (referred to as *pyevdev gestures*), or from any DBus source (see e.g. [newm-hand-gestures](https://github.com/jbuchermn/newm-hand-gestures) for an implementation based on a webcam and you moving your hands in front of the laptop).

The reason for having c, as well as python gestures, is that libinput handles gestures very poorly - e.g. it's not possible to detect the end (finger lifted from touchpad) of gestures. But (see also the
troubleshooting section), python-side gestures are less secure as your user needs access to the device and newm can't rely on seat management.

The following keys configure the providers:

| Configuration key                       | Default value                          | Description                                                                       |
| --------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------- |
| `gestures.c.enabled`                    |`True`                                  | Enable c gestures                                                                 |
| `gestures.c.scale_px`                   |`800.`                                  | Scaling of c gestures (just experiment with it)                                   |
| `gestures.dbus.enabled`                 |`True`                                  | Allow DBus gestures                                                               |
| `gestures.pyevdev.enabled`              |`False`                                 | Enable python gestures (very much encouraged!)                                    |
| `gestures.pyevdev.two_finger_min_dist`  |`.1`                                    | Experiment with this                                                              |
| `gestures.pyevdev.validate_threshold`   |`.02`                                   | Experiment with this                                                              |


### Config: Panels

Panels mean UI elements, or clients with some special behaviour:

- `launcher`: Application launcher, which can be slid in using a gesture
- `lock`: Lock screen
- `top_bar`, `bottom_bar`, `bar`: Bars

These are in general separate apps and can be developed independently of newm; they are started (and restarted, if necessary) by newm and establish a connection to the compositor via dbus. For the bars, there is a newm-included simple implementation
which can be configured using `panels.top_bar.native` (`panels.bottom_bar.native`). It is, however, not nearly as powerful, as e.g. `waybar`.

By default **newm_panel_basic** is included, where the first two of these are implemented as terminal applications in a very basic manner.

| Configuration key                       | Default value                            | Description                                                                                     |
| --------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `panels.launcher.cmd`                   |`"alacritty -e newm-panel-basic launcher"`| Command to start launcher panel                                                                 |
| `panels.lock.cmd`                       |`"alacritty -e newm-panel-basic lock"`    | Command to start lock panel                                                                     |
| `panels.bar.cmd`                        |`None`                                    | Command to start top and bottom bars (e.g. `waybar`)                                            |
| `panels.top_bar.cmd`                    |`None`                                    | Command to start top bar (if not started by `bar` command or native bar in use)                 |
| `panels.bottom_bar.cmd`                 |`None`                                    | Command to start bottom bar (if not started by `bar` command or native bar in use)              |
| `panels.launcher.cwd`                   |`None`                                    | Working directory for corresponding command                                                     |
| `panels.lock.cwd`                       |`None`                                    | Working directory for corresponding command                                                     |
| `panels.top_bar.cwd`                    |`None`                                    | Working directory for corresponding command                                                     |
| `panels.bottom_bar.cwd`                 |`None`                                    | Working directory for corresponding command                                                     |
| `panels.bar.cwd`                        |`None`                                    | Working directory for corresponding command                                                     |
| `panels.launcher.corner_radius`         |`0`                                       | Launcher panel: corner radius (pixel)                                                           |
| `panels.launcher.gesture_factor`        |`200`                                     | Higher number means less movement with 5 fingers is necessary to open launcher panel            |
| `panels.launcher.h`                     |`0.8`                                     | Launcher panel: height (`1.0` is full height)                                                   |
| `panels.launcher.w`                     |`0.8`                                     | Launcher panel: width (`1.0` is full width)                                                     |
| `panels.launcher.x`                     |`0`                                       | Launcher panel: x position (Can fix issues for some outputs placements)                         |
| `panels.launcher.y`                     |`0`                                       | Launcher panel: y position (Can fix issues for some outputs placements)                         |
| `panels.lock.corner_radius`             |`50`                                      | Lock panel: corner radius (pixel)                                                               |
| `panels.lock.h`                         |`0.6`                                     | Lock panel: height (`1.0` is full height)                                                       |
| `panels.lock.w`                         |`0.7`                                     | Lock panel: width (`1.0` is full width)                                                         |
| `panels.lock.x`                         |`0`                                       | Lock panel: x position (Can fix issues for some outputs placements)                             |
| `panels.lock.y`                         |`0`                                       | Lock panel: y position (Can fix issues for some outputs placements)                             |
| `panels.bar.visible_fullscreen`         |`False`                                   | Should the bars be visible in fullscreen mode?                                                  |
| `panels.bar.visible_normal`             |`True`                                    | Should the bars be visible in normal mode (or only if the overview is shown)?                   |
| `panels.top_bar.visible_fullscreen`     |`False`                                   | Analogous to `panels.bar.visible_fullscreen`                                                    |
| `panels.top_bar.visible_normal`         |`True`                                    | Analogous to `panels.bar.visible_normal`                                                        |
| `panels.bottom_bar.visible_fullscreen`  |`False`                                   | Analogous to `panels.bar.visible_fullscreen`                                                    |
| `panels.bottom_bar.visible_normal`      |`True`                                    | Analogous to `panels.bar.visible_normal`                                                        |
| `panels.top_bar.native.enabled`         |`False`                                   | Enable native top bar                                                                           |
| `panels.top_bar.native.font`            |`'Source Code Pro for Powerline'`         | Font for native top bar                                                                         |
| `panels.top_bar.native.font_size`       |`12`                                      | Font size for native top bar                                                                    |
| `panels.top_bar.native.height`          |`20`                                      | Height of native top bar                                                                        |
| `panels.top_bar.native.texts`           |`lambda: ["1", "2", "3"]`                 | Function called each time top bar is rendered producing the text to render                      |
| `panels.bottom_bar.native.enabled`      |`False`                                   | Enable native bottom bar                                                                        |
| `panels.bottom_bar.native.font`         |`'Source Code Pro for Powerline'`         | Font for native bottom bar                                                                      |
| `panels.bottom_bar.native.font_size`    |`12`                                      | Font size for native bottom bar                                                                 |
| `panels.bottom_bar.native.height`       |`20`                                      | Height of native bottom bar                                                                     |
| `panels.bottom_bar.native.texts`        |`lambda: ["4", "5", "6"]`                 | Function called each time bottom bar is rendered producing the text to render                   |

The values for `panels.lock.x/y` and `panels.launcher.x/y` will be added to the default values that is calculated by NEWM. This is useful if one of your secondaries outputs is placed below your main one since it's where the panels are placed by default when inactive.

The basic launcher panel is configured using `~/.config/newm/launcher.py`, e.g.

```py
entries = {
    "chromium": "chromium --enable-features=UseOzonePlatform --ozone-platform=wayland",
    "alacritty": "alacritty"
}
shortcuts = {
    1: ("chromium", "chromium --enable-features=UseOzonePlatform --ozone-platform=wayland"),
    2: ("alacritty", "alacritty")
}
```

provides ways to start chromium and alacritty either by typing their names, or by using the keys 1 and 2 when the launcher is open.

### Config: helpers

The package `newm.helpers` provide some behaviour (smooth dimming, pulse audio, `wob` support),
that's very convenient and can be expected in a compositor, but is not really part of it.

These methods can be used or ignored freely when configuring newm (see e.g. [default_config.py](https://github.com/jbuchermn/newm/blob/master/newm/default_config.py) or [dotfiles-nix](https://github.com/jbuchermn/dotfiles-nix)) for examples.

The code is very simple and straight-forward, so I suggest reading through the corresponding files for details.
