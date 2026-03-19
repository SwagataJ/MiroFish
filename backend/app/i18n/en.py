"""English message dictionary for API responses."""

MESSAGES = {
    # Project management
    "project_not_found": "Project not found: {project_id}",
    "project_deleted": "Project deleted: {project_id}",
    "project_delete_failed": "Project not found or delete failed: {project_id}",
    "project_reset": "Project reset: {project_id}",

    # Ontology generation
    "provide_sim_requirement": "Please provide simulation requirement (simulation_requirement)",
    "provide_files": "Please upload at least one document file",
    "no_docs_processed": "No documents were processed successfully. Please check file formats.",
    "config_error": "Configuration error: {errors}",

    # Graph building
    "provide_project_id": "Please provide project_id",
    "ontology_not_generated": "Ontology not yet generated. Please call /ontology/generate first.",
    "graph_building_in_progress": "Graph is currently being built. Do not resubmit. To force rebuild, add force: true",
    "graph_build_started": "Graph build task started. Query progress via /task/{task_id}",
    "extracted_text_not_found": "Extracted text content not found",
    "ontology_not_found": "Ontology definition not found",

    # Task messages
    "task_not_found": "Task not found: {task_id}",
    "init_graph_build": "Initializing graph build service...",
    "chunking_text": "Chunking text...",
    "creating_zep_graph": "Creating Zep graph...",
    "setting_ontology": "Setting ontology definition...",
    "adding_chunks": "Adding {count} text chunks...",
    "waiting_zep": "Waiting for Zep to process data...",
    "fetching_graph_data": "Fetching graph data...",
    "graph_build_complete": "Graph build complete",
    "build_failed": "Build failed: {error}",

    # Graph data & deletion
    "graph.deleted": "Graph deleted: {graph_id}",

    # Simulation
    "sim_not_found": "Simulation not found: {simulation_id}",
    "entity_not_found": "Entity not found: {entity_uuid}",
    "zep_not_configured": "ZEP_API_KEY not configured",

    # Simulation - create
    "sim.graph_not_built": "Graph not yet built for this project. Please call /api/graph/build first.",

    # Simulation - prepare
    "sim.already_prepared": "Preparation already completed, no need to regenerate",
    "sim.prepare_started": "Preparation task started. Query progress via /api/simulation/prepare/status",
    "sim.missing_sim_requirement": "Project is missing simulation requirement (simulation_requirement)",
    "sim.prepare_not_started": "Preparation not started yet. Please call /api/simulation/prepare to begin",
    "sim.prepare_task_completed": "Task completed (preparation already exists)",
    "sim.already_prepared_status": "Preparation already completed",

    # Simulation - config
    "sim.config_not_found": "Simulation config not found. Please call /prepare first.",
    "sim.config_file_not_found": "Config file not found. Please call /prepare first.",

    # Simulation - scripts
    "sim.unknown_script": "Unknown script: {script_name}. Available: {allowed_scripts}",
    "sim.script_not_found": "Script file not found: {script_name}",

    # Simulation - profiles
    "sim.no_matching_entities": "No matching entities found",

    # Simulation - run control
    "sim.provide_simulation_id": "Please provide simulation_id",
    "sim.max_rounds_positive": "max_rounds must be a positive integer",
    "sim.max_rounds_invalid": "max_rounds must be a valid integer",
    "sim.invalid_platform": "Invalid platform type: {platform}. Options: twitter/reddit/parallel",
    "sim.already_running": "Simulation is currently running. Please call /stop first, or use force=true to force restart.",
    "sim.not_ready": "Simulation not ready. Current status: {status}. Please call /prepare first.",
    "sim.graph_memory_requires_graph": "Enabling graph memory update requires a valid graph_id. Please ensure the project has a built graph.",
    "sim.db_not_exists": "Database does not exist. Simulation may not have run yet.",

    # Simulation - interview
    "sim.provide_agent_id": "Please provide agent_id",
    "sim.provide_prompt": "Please provide prompt (interview question)",
    "sim.platform_invalid": "platform parameter must be 'twitter' or 'reddit'",
    "sim.env_not_running": "Simulation environment is not running or has been closed. Please ensure the simulation has completed and entered command-waiting mode.",
    "sim.provide_interviews": "Please provide interviews (interview list)",
    "sim.interview_missing_agent_id": "Interview list item {index} is missing agent_id",
    "sim.interview_missing_prompt": "Interview list item {index} is missing prompt",
    "sim.interview_invalid_platform": "Interview list item {index} platform must be 'twitter' or 'reddit'",
    "sim.interview_timeout": "Interview response timed out: {error}",
    "sim.batch_interview_timeout": "Batch interview response timed out: {error}",
    "sim.global_interview_timeout": "Global interview response timed out: {error}",

    # Simulation - env status
    "sim.env_running": "Environment is running and can accept Interview commands",
    "sim.env_not_available": "Environment is not running or has been closed",
    "sim.env_close_sent": "Environment close command sent",

    # Simulation - prepare progress stages
    "sim.stage_reading": "Reading graph entities",
    "sim.stage_generating_profiles": "Generating agent profiles",
    "sim.stage_generating_config": "Generating simulation config",
    "sim.stage_copying_scripts": "Preparing simulation scripts",
    "sim.prepare_env_started": "Starting simulation environment preparation...",

    # Report
    "report_not_found": "Report not found",
    "report.not_found_id": "Report not found: {report_id}",
    "report_exists": "Report already exists",
    "report_generating": "Report generation task started",
    "report.generating_started": "Report generation task started. Query progress via /api/report/generate/status",
    "report_gen_failed": "Report generation failed",
    "missing_graph_id": "Missing graph ID. Please ensure graph has been built.",
    "missing_sim_requirement": "Missing simulation requirement description",

    # Report - provide params
    "report.provide_simulation_id": "Please provide simulation_id",
    "report.provide_task_or_sim_id": "Please provide task_id or simulation_id",
    "report.provide_message": "Please provide message",
    "report.provide_graph_id_and_query": "Please provide graph_id and query",
    "report.provide_graph_id": "Please provide graph_id",
    "report.missing_graph_id": "Missing graph ID",
    "report.report_generated": "Report has been generated",
    "report.deleted": "Report deleted: {report_id}",
    "report.no_report_for_sim": "No report found for this simulation: {simulation_id}",
    "report.progress_not_available": "Report not found or progress info not available: {report_id}",
    "report.section_not_found": "Section not found: section_{section_index}.md",
    "report.init_agent": "Initializing Report Agent...",

    # Generic
    "unknown_error": "Unknown error",
    "provide_task_id_or_sim_id": "Please provide task_id or simulation_id",
}
