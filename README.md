# `action-build-cmake`

> Builds the project using CMake. **Requires the `phlex-ci` container**.

## Usage

```yaml
- uses: Framework-R-D/action-build-cmake@30bca0b2d76e90cf1cc9e6e863aed5be505e7e61 # v1
  with:
    input-name: value
```

## Inputs

| Name | Description | Required | Default |
|------|-------------|----------|---------|
| `source-path` | Path where source code is checked out | false | `phlex-src` |
| `build-path` | Path for build directory | false | `phlex-build` |
| `target` | CMake target to build (empty for default target) | false | `` |
| `parallel-jobs` | Number of parallel jobs (empty for auto-detect) | false | `` |

## Outputs

| Name | Description |
|------|-------------|
(none)

## License

[Apache 2.0](LICENSE)

## Notes

`target` is a single CMake target argument, not a shell- or whitespace-separated option list; leading options and line breaks are rejected. `parallel-jobs` must be a positive integer. Building still executes the configured source/build scripts and requires caller-authorized source and trusted compiler/tool configuration; safe argument quoting is not approval of fork code. CI yamllint is installed from the immutable workflow checkout's locked uv manifest, tracked by Dependabot, and only the CodeQL job has `security-events: write`.

> [!NOTE]
> This action requires the `ghcr.io/framework-r-d/phlex-ci` container image
> (sources `/entrypoint.sh` to activate the Spack environment).
> It is not a general-purpose action.
