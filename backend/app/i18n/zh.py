"""Chinese message dictionary for API responses."""

MESSAGES = {
    # Project management
    "project_not_found": "项目不存在: {project_id}",
    "project_deleted": "项目已删除: {project_id}",
    "project_delete_failed": "项目不存在或删除失败: {project_id}",
    "project_reset": "项目已重置: {project_id}",

    # Ontology generation
    "provide_sim_requirement": "请提供模拟需求描述 (simulation_requirement)",
    "provide_files": "请至少上传一个文档文件",
    "no_docs_processed": "没有成功处理任何文档，请检查文件格式",
    "config_error": "配置错误: {errors}",

    # Graph building
    "provide_project_id": "请提供 project_id",
    "ontology_not_generated": "项目尚未生成本体，请先调用 /ontology/generate",
    "graph_building_in_progress": "图谱正在构建中，请勿重复提交。如需强制重建，请添加 force: true",
    "graph_build_started": "图谱构建任务已启动，请通过 /task/{task_id} 查询进度",
    "extracted_text_not_found": "未找到提取的文本内容",
    "ontology_not_found": "未找到本体定义",

    # Task messages
    "task_not_found": "任务不存在: {task_id}",
    "init_graph_build": "初始化图谱构建服务...",
    "chunking_text": "文本分块中...",
    "creating_zep_graph": "创建Zep图谱...",
    "setting_ontology": "设置本体定义...",
    "adding_chunks": "开始添加 {count} 个文本块...",
    "waiting_zep": "等待Zep处理数据...",
    "fetching_graph_data": "获取图谱数据...",
    "graph_build_complete": "图谱构建完成",
    "build_failed": "构建失败: {error}",

    # Graph data & deletion
    "graph.deleted": "图谱已删除: {graph_id}",

    # Simulation
    "sim_not_found": "模拟不存在: {simulation_id}",
    "entity_not_found": "实体不存在: {entity_uuid}",
    "zep_not_configured": "ZEP_API_KEY未配置",

    # Simulation - create
    "sim.graph_not_built": "项目尚未构建图谱，请先调用 /api/graph/build",

    # Simulation - prepare
    "sim.already_prepared": "已有完成的准备工作，无需重复生成",
    "sim.prepare_started": "准备任务已启动，请通过 /api/simulation/prepare/status 查询进度",
    "sim.missing_sim_requirement": "项目缺少模拟需求描述 (simulation_requirement)",
    "sim.prepare_not_started": "尚未开始准备，请调用 /api/simulation/prepare 开始",
    "sim.prepare_task_completed": "任务已完成（准备工作已存在）",
    "sim.already_prepared_status": "已有完成的准备工作",

    # Simulation - config
    "sim.config_not_found": "模拟配置不存在，请先调用 /prepare 接口",
    "sim.config_file_not_found": "配置文件不存在，请先调用 /prepare 接口",

    # Simulation - scripts
    "sim.unknown_script": "未知脚本: {script_name}，可选: {allowed_scripts}",
    "sim.script_not_found": "脚本文件不存在: {script_name}",

    # Simulation - profiles
    "sim.no_matching_entities": "没有找到符合条件的实体",

    # Simulation - run control
    "sim.provide_simulation_id": "请提供 simulation_id",
    "sim.max_rounds_positive": "max_rounds 必须是正整数",
    "sim.max_rounds_invalid": "max_rounds 必须是有效的整数",
    "sim.invalid_platform": "无效的平台类型: {platform}，可选: twitter/reddit/parallel",
    "sim.already_running": "模拟正在运行中，请先调用 /stop 接口停止，或使用 force=true 强制重新开始",
    "sim.not_ready": "模拟未准备好，当前状态: {status}，请先调用 /prepare 接口",
    "sim.graph_memory_requires_graph": "启用图谱记忆更新需要有效的 graph_id，请确保项目已构建图谱",
    "sim.db_not_exists": "数据库不存在，模拟可能尚未运行",

    # Simulation - interview
    "sim.provide_agent_id": "请提供 agent_id",
    "sim.provide_prompt": "请提供 prompt（采访问题）",
    "sim.platform_invalid": "platform 参数只能是 'twitter' 或 'reddit'",
    "sim.env_not_running": "模拟环境未运行或已关闭。请确保模拟已完成并进入等待命令模式。",
    "sim.provide_interviews": "请提供 interviews（采访列表）",
    "sim.interview_missing_agent_id": "采访列表第{index}项缺少 agent_id",
    "sim.interview_missing_prompt": "采访列表第{index}项缺少 prompt",
    "sim.interview_invalid_platform": "采访列表第{index}项的platform只能是 'twitter' 或 'reddit'",
    "sim.interview_timeout": "等待Interview响应超时: {error}",
    "sim.batch_interview_timeout": "等待批量Interview响应超时: {error}",
    "sim.global_interview_timeout": "等待全局Interview响应超时: {error}",

    # Simulation - env status
    "sim.env_running": "环境正在运行，可以接收Interview命令",
    "sim.env_not_available": "环境未运行或已关闭",
    "sim.env_close_sent": "环境关闭命令已发送",

    # Simulation - prepare progress stages
    "sim.stage_reading": "读取图谱实体",
    "sim.stage_generating_profiles": "生成Agent人设",
    "sim.stage_generating_config": "生成模拟配置",
    "sim.stage_copying_scripts": "准备模拟脚本",
    "sim.prepare_env_started": "开始准备模拟环境...",

    # Report
    "report_not_found": "报告不存在",
    "report.not_found_id": "报告不存在: {report_id}",
    "report_exists": "报告已存在",
    "report_generating": "报告生成任务已启动",
    "report.generating_started": "报告生成任务已启动，请通过 /api/report/generate/status 查询进度",
    "report_gen_failed": "报告生成失败",
    "missing_graph_id": "缺少图谱ID，请确保已构建图谱",
    "missing_sim_requirement": "缺少模拟需求描述",

    # Report - provide params
    "report.provide_simulation_id": "请提供 simulation_id",
    "report.provide_task_or_sim_id": "请提供 task_id 或 simulation_id",
    "report.provide_message": "请提供 message",
    "report.provide_graph_id_and_query": "请提供 graph_id 和 query",
    "report.provide_graph_id": "请提供 graph_id",
    "report.missing_graph_id": "缺少图谱ID",
    "report.report_generated": "报告已生成",
    "report.deleted": "报告已删除: {report_id}",
    "report.no_report_for_sim": "该模拟暂无报告: {simulation_id}",
    "report.progress_not_available": "报告不存在或进度信息不可用: {report_id}",
    "report.section_not_found": "章节不存在: section_{section_index}.md",
    "report.init_agent": "初始化Report Agent...",

    # Generic
    "unknown_error": "未知错误",
    "provide_task_id_or_sim_id": "请提供 task_id 或 simulation_id",
}
