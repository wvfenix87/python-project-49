lint:
	uv run ruff check brain_games

brain-games:
	uv run start-game -t even

build:
	uv build

package-install:
	uv tool install  --force dist/*.whl