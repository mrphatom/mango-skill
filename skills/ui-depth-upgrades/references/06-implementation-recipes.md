# 06 - Implementation Recipes

Cross-platform patterns for the three moves.

## Web (HTML/CSS)
- Move 1: absolute positioning + negative margins or transform: scale on the subject; z-index stacking; text-shadow or -webkit-text-stroke for overlap legibility.
- Move 2: background-image on a full-bleed container; linear-gradient scrim; backdrop-filter: blur() on panels with solid fallback.
- Move 3: CSS clip-path with the output of `scalloped_mask.py --format clip`; SVG textPath for curved lettering.

## React Native
- Use absolute positioning inside a relative parent.
- For blur: expo-blur or @react-native-community/blur with platform checks.
- Clip paths via react-native-svg MaskedView or Skia.

## SwiftUI
- .overlay + .offset + .scaleEffect for oversized subject.
- .background with Image + .blur + Color.black.opacity for scrims.
- Custom Shape for scalloped crops.

## Jetpack Compose
- Box + Modifier.offset + graphicsLayer for scale/z.
- Brush.verticalGradient for scrims.
- Path + clipPath for custom crops.

Start from the HTML templates in `assets/templates/` and adapt.
