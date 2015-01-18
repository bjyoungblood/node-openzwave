{
  "targets": [
    {
      "target_name": "openzwave",
      "sources": [
        "src/openzwave.cc"
      ],
      "include_dirs": [
        "deps/openzwave/cpp/src"
        "deps/openzwave/cpp/hidapi/hidapi",
        "deps/openzwave/cpp/src",
        "deps/openzwave/cpp/src/command_classes",
        "deps/openzwave/cpp/src/platform",
        "deps/openzwave/cpp/src/platform/unix",
        "deps/openzwave/cpp/src/value_classes",
        "deps/openzwave/cpp/tinyxml"
      ],
      "dependencies": [
        "deps/libopenzwave.gyp:libopenzwave"
      ]
    }
  ]
}
