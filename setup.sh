#!/bin/bash

echo "🚀 GitLab Docker 环境管理脚本"
echo "==============================="
echo

# 检查是否有 Node.js/npm
if command -v npm &> /dev/null; then
    echo "✅ 检测到 npm，使用优化的脚本命令"
    echo
    echo "📖 可用命令："
    echo "  npm run start     - 启动GitLab环境"
    echo "  npm run stop      - 停止GitLab环境"
    echo "  npm run status    - 查看服务状态"
    echo "  npm run logs      - 查看服务日志"
    echo "  npm run cleanup   - 清理Docker资源"
    echo "  npm run help      - 查看所有命令"
    echo
    echo "💡 推荐: 运行 'npm run help' 查看完整说明"
    echo "⚡ 快速启动: 'npm run start'"
else
    echo "⚠️  未检测到 npm，使用传统 docker-compose 命令"
    echo
    echo "📖 可用命令："
    echo "  docker compose up -d     - 启动服务"
    echo "  docker compose down      - 停止服务"
    echo "  docker compose ps        - 查看状态"
    echo "  docker compose logs -f   - 查看日志"
fi

echo
echo "💰 成本优化提示："
echo "  - 使用完毕后记得停止服务以节省 Codespaces 资源"
echo "  - 定期清理 Docker 镜像以释放磁盘空间"
echo "  - 考虑在不活跃时暂停 Codespace"
echo