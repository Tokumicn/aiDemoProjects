.PHONY: all install fix lint lint-ci test run clean export lock miration help

# 默认命令  输入 make 则直接执行 make all
.DEFAULT_GOAL := all

# 本地开发一键就绪： 安装依赖 -> 自动修复 -> 严格检查
all: install fix lint

# 安装依赖
# 使用 XXX 镜像源安装所有依赖
install:
	# 安装运行依赖 + 开发、测试依赖  确保 ruff/mypy 等工具可用
	uv sync --all-extras --group dev --group lint --group test --index-url https://bytedpypi.byted.org/simple


# ===================
#       代码质量
# ===================

# ======================
# 主动修复工具 - 本地开发用
# ======================
# 包含： 格式化代码 + 自动修复逻辑错误 + 自动排序 import
fix:
	# 1. 排版(空格、换行、缩进)
	uv run ruff format .
	# 2. 逻辑检查 (去除未使用引用、import排序等)
	uv run ruff check --fix .
	# 3. 静态类型检查
	uv run mypy .


# ======================
# 被动修复工具 - CI/CD用
# ======================
# 只读：不修改文件，只报错
lint:
	uv run ruff format --check .
	uv run ruff check .
	uv run mypy .

# CI 调用入口
lint-ci: install lint


# ======================
# 开发工具
# ======================

# 单元测试
test:
	PYTHONPATH=. uv run pytest tests

test-ci: install test


# 导出依赖
# 生成 requirements.txt 兼容不支持 uv 的项目
export:
	uv export --format requirements.txt > requirements.txt

# 锁定依赖
# 仅更新 uv.lock 文件，不安装
lock:
	uv lock

# 数据迁移
migration:
	uv run python3 command.py migrate up

# 运行主程序
run:
	uv run python main.py

# 清理缓存
clean:
	rm -rf .ruff_cache .mypy_cache .pytest_cache
	find . -type -d -name "__pycache__" -exec rm -rf {} +
