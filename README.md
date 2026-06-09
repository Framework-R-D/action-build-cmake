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

> [!NOTE]
> This action requires the `ghcr.io/framework-r-d/phlex-ci` container image
> (sources `/entrypoint.sh` to activate the Spack environment).
> It is not a general-purpose action.
