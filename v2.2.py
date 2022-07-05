{
    # region General
    "settings_lists": [
        "All Settings (Please refer to docs to learn more about):\n%s",
        "所有设置（具体数值含义请自行查看文档）：\n%s"
    ],
    "cmd_err_run": [
        f"Error occurred when running command: {code('%s')}: {code('%s')}\n{code('%s')}",
        f"运行指令 {code('%s')} 时发生错误: {code('%s')}\n{code('%s')}",
    ],
    "no_cmd_given": [
        "Please use this command in private chat, or add parameters to execute.",
        "请在私聊时使用此命令，或添加参数执行。"
    ],
    "invalid_user_id": [
        "Invalid User ID",
        "未知用户或无效的用户 ID"
    ],
    "invalid_param": [
        "Invalid Parameter",
        "无效的参数"
    ],
    "enabled": [
        "Enabled",
        "开启"
    ],
    "disabled": [
        "Disabled",
        "关闭"
    ],
    "none": [
        "None",
        "无"
    ],
    "tip_edit": [
        f"You can edit this by using {code('%s')}",
        f"如需编辑，请使用 {code('%s')}"
    ],
    "tip_run_in_pm": [
        "You can only run this command in private chat, or by adding parameters.",
        "请在私聊使用此命令，或添加参数执行。"
    ],
    # endregion

    # region Plugin
    "plugin_desc": [
        "Captcha for PM",
        "私聊人机验证插件"
    ],
    "check_usage": [
        "Please use %s to see available commands.",
        "请使用 %s 查看可用命令"
    ],
    "curr_version": [
        f"Current {code('PMCaptcha')} Version: %s",
        f"{code('PMCaptcha')} 当前版本：%s"
    ],
    "unknown_version": [
        italic("Unknown"),
        italic("未知")
    ],
    # endregion

    # region Vocabs
    "vocab_msg": [
        "Message",
        "消息"
    ],
    "vocab_array": [
        "List",
        "列表"
    ],
    "vocab_bool": [
        "Boolean",
        "y / n"
    ],
    "vocab_int": [
        "Integer",
        "整数"
    ],
    "vocab_cmd": [
        "Command",
        "指令"
    ],
    "vocab_rule": [
        "Rule",
        "规则"
    ],
    "vocab_action": [
        "Action",
        "操作"
    ],
    # endregion

    # region Captcha Challenge
    "verify_verified": [
        "Verified user",
        "已验证用户"
    ],
    "verify_unverified": [
        "Unverified user",
        "未验证用户"
    ],
    "verify_blocked": [
        "You were blocked.",
        "您已被封禁"
    ],
    "verify_log_punished": [
        "User %s has been %s.",
        "已对用户 %s 执行`%s`操作"
    ],
    "verify_log_passed": [
        "User %s has passed the %s captcha.",
        "用户 %s 已通过`%s`验证"
    ],
    "verify_challenge": [
        "Please answer this question to prove you are human (1 chance)",
        "请回答这个问题证明您不是机器人 (一次机会)"
    ],
    "verify_challenge_timed": [
        "You have %i seconds.",
        "您有 %i 秒来回答这个问题"
    ],
    "verify_passed": [
        "Verification passed.",
        "验证通过"
    ],
    "verify_failed": [
        "Verification failed.",
        "验证失败"
    ],
    "verify_timeout": [
        "Verification timeout.",
        "验证超时"
    ],
    # Image
    "verify_complete_image": [
        "Please complete the following image captcha.",
        "请完成以下图像辨识验证"
    ],
    # Sticker
    "verify_send_sticker": [
        "Please send a sticker to me.",
        "请发送一个贴纸给我"
    ],
    # endregion

    # region Help
    "cmd_param": [
        "Parameter",
        "参数"
    ],
    "cmd_param_optional": [
        "Optional",
        "可选"
    ],
    "cmd_alias": [
        "Alias",
        "别名/快捷命令"
    ],
    "cmd_detail": [
        f"Do {code(f',{user_cmd_name} h ')}[command ] for details",
        f"详细指令请输入 {code(f',{user_cmd_name} h ')}[指令名称 ]",
    ],
    "cmd_not_found": [
        "Command Not Found",
        "指令不存在"
    ],
    "cmd_list": [
        "Command List",
        "指令列表"
    ],
    "priority": [
        "Priority",
        "优先级"
    ],
    "cmd_search_result": [
        f"Search Result for `%s`",
        f"`%s` 的搜索结果"
    ],
    "cmd_search_docs": [
        "Documentation",
        "文档"
    ],
    "cmd_search_cmds": [
        "Commands",
        "指令"
    ],
    "cmd_search_none": [
        "No result found.",
        "未找到结果"
    ],
    # endregion

    # region Check
    "user_verified": [
        f"User {code('%i')} {italic('verified')}",
        f"用户 {code('%i')} {italic('已验证')}"
    ],
    "user_unverified": [
        f"User {code('%i')} {bold('unverified')}",
        f"用户 {code('%i')} {bold('未验证')}"
    ],
    # endregion

    # region Add / Delete
    "add_whitelist_success": [
        f"User {code('%i')} added to whitelist",
        f"用户 {code('%i')} 已添加到白名单"
    ],
    "add_whitelist_failed": [
        f"Failed to add iser {code('%i')} to whitelist",
        f"无法添加用户 {code('%i')} 到白名单"
    ],
    "remove_verify_log_success": [
        f"Removed User {code('%i')}'s verify record",
        f"已删除用户 {code('%i')} 的验证记录"
    ],
    "remove_verify_log_failed": [
        f"Failed to remove User {code('%i')}'s verify record.",
        f"删除用户 {code('%i')} 的验证记录失败"
    ],
    "remove_verify_log_not_found": [
        f"Verify record not found for User {code('%i')}",
        f"未找到用户 {code('%i')} 的验证记录"
    ],
    # endregion

    # region Unstuck
    "unstuck_success": [
        f"User {code('%i')} has removed from challenge mode",
        f"用户 {code('%i')} 已解除验证状态"
    ],
    "not_stuck": [
        f"User {code('%i')} is not stuck",
        f"用户 {code('%i')} 未在验证状态"
    ],
    # endregion

    # region Welcome
    "welcome_curr_rule": [
        "Current welcome rule",
        "当前验证通过时消息规则"
    ],
    "welcome_set": [
        "Welcome message set.",
        "已设置验证通过消息"
    ],
    "welcome_reset": [
        "Welcome message reset.",
        "已重置验证通过消息"
    ],
    # endregion

    # region Whitelist
    "whitelist_curr_rule": [
        "Current whitelist rule",
        "当前白名单规则"
    ],
    "whitelist_set": [
        "Keywords whitelist set.",
        "已设置关键词白名单"
    ],
    "whitelist_reset": [
        "Keywords whitelist reset.",
        "已重置关键词白名单"
    ],
    # endregion

    # region Blacklist
    "blacklist_curr_rule": [
        "Current blacklist rule",
        "当前黑名单规则"
    ],
    "blacklist_set": [
        "Keywords blacklist set.",
        "已设置关键词黑名单"
    ],
    "blacklist_reset": [
        "Keywords blacklist reset.",
        "已重置关键词黑名单"
    ],
    "blacklist_triggered": [
        "Blacklist rule triggered",
        "您触发了黑名单规则"
    ],
    # endregion

    # region Timeout
    "timeout_curr_rule": [
        "Current timeout: %i second(s)",
        "当前超时时间: %i 秒"
    ],
    "timeout_set": [
        "Verification timeout has been set to %i seconds.",
        "已设置验证超时时间为 %i 秒"
    ],
    "timeout_off": [
        "Verification timeout disabled.",
        "已关闭验证超时时间"
    ],
    "timeout_exceeded": [
        "Verification timeout.",
        "验证超时"
    ],
    # endregion

    # region Disable PM
    "disable_pm_curr_rule": [
        "Current disable PM status: %s",
        "当前禁止私聊状态: 已%s"
    ],
    "disable_pm_tip_exception": [
        "This feature will automatically allow contents and whitelist users.",
        "此功能会自动放行联系人与白名单用户"
    ],
    "disable_set": [
        f"Disable private chat has been set to {bold('%s')}.",
        f"已设置禁止私聊为{bold('%s')}"
    ],
    "disable_pm_enabled": [
        "Owner has private chat disabled.",
        "对方已禁止私聊。"
    ],
    # endregion

    # region Stats
    "stats_display": [
        "has verified %i users in total.\nSuccess: %i\nBlocked: %i",
        "已进行验证 %i 次\n验证通过: %i 次\n拦截: %i 次"
    ],
    "stats_reset": [
        "Statistics has been reset.",
        "已重置统计"
    ],
    # endregion

    # region Action
    "action_curr_rule": [
        "Current action rule",
        "当前验证失败规则"
    ],
    "action_set": [
        f"Action has been set to {bold('%s')}.",
        f"验证失败后将执行{bold('%s')}操作"
    ],
    "action_set_none": [
        "Action has been set to none.",
        "验证失败后将不执行任何操作"
    ],
    "action_ban": [
        "Ban",
        "封禁"
    ],
    "action_delete": [
        "Ban and delete",
        "封禁并删除对话"
    ],
    "action_archive": [
        "Ban and archive",
        "封禁并归档"
    ],
    # endregion

    # region Report
    "report_curr_rule": [
        "Current report state: %s",
        "当前举报状态为: %s"
    ],
    "report_set": [
        f"Report has been set to {bold('%s')}.",
        f"已设置举报状态为{bold('%s')}"
    ],
    # endregion

    # region Premium
    "premium_curr_rule": [
        "Current premium user rule",
        "当前 Premium 用户规则"
    ],
    "premium_set_allow": [
        f"Telegram Premium users will be allowed to {bold('bypass')} the captcha.",
        f"将{bold('不对')} Telegram Premium 用户{bold('发起验证')}"
    ],
    "premium_set_ban": [
        f"Telegram Premium users will be {bold('banned')} from private chat.",
        f"将{bold('禁止')} Telegram Premium 用户私聊"
    ],
    "premium_set_only": [
        f"{bold('Only allowed')} Telegram Premium users to private chat.",
        f"将{bold('仅允许')} Telegram Premium 用户私聊"
    ],
    "premium_set_none": [
        "Nothing will do to Telegram Premium",
        "将不对 Telegram Premium 用户执行额外操作"
    ],
    "premium_only": [
        "Owner only allows Telegram Premium users to private chat.",
        "对方只允许 Telegram Premium 用户私聊"
    ],
    "premium_ban": [
        "Owner bans Telegram Premium users from private chat.",
        "对方禁止 Telegram Premium 用户私聊"
    ],
    # endregion

    # region Groups In Common
    "groups_in_common_curr_rule": [
        "Current groups in common rule",
        "当前共同群规则"
    ],
    "groups_in_common_set": [
        f"Groups in common larger than {bold('%i')} will be whitelisted.",
        f"共同群数量大于 {bold('%i')} 时将自动添加到白名单"
    ],
    "groups_in_common_disabled": [
        "Group in command is not enabled",
        "未开启共同群数量检测"
    ],
    "groups_in_common_disable": [
        "Groups in common disabled.",
        "已关闭共同群检查"
    ],
    # endregion

    # region Chat History
    "chat_history_curr_rule": [
        f"Chat history equal or larger than {bold('%i')} will be whitelisted.",
        f"聊天记录数量大于 {bold('%i')} 时将自动添加到白名单"
    ],
    "chat_history_disabled": [
        "Chat history check is not enabled",
        "未开启聊天记录数量检测"
    ],
    # endregion

    # region Initiative
    "initiative_curr_rule": [
        "Current initiative status: %s",
        "当前对主动进行对话的用户添加白名单状态为： %s"
    ],
    "initiative_set": [
        f"Initiative has been set to {bold('%s')}.",
        f"已设置对主动进行对话的用户添加白名单状态为{bold('%s')}"
    ],
    # endregion

    # region Silent
    "silent_curr_rule": [
        "Current silent status: %s",
        "当前静音状态: 已%s"
    ],
    "silent_set": [
        f"Silent has been set to {bold('%s')}.",
        f"已设置静音模式为{bold('%s')}"
    ],
    # endregion

    # region Flood
    "flood_curr_rule": [
        "Current flood detect limit was set to %i user(s)",
        "当前轰炸人数已设置为 %i 人"
    ],
    # Username
    "flood_username_curr_rule": [
        "Current flood username option was set to %s",
        "当前轰炸时切换用户名选项已设置为 %s"
    ],
    "flood_username_set_confirm": [
        (f"The feature may lose your username, are you sure you want to enable this feature?\n"
         f"Please enter {code(f',{cmd_name} flood_username y')} again to confirm."),
        f"此功能有可能会导致您的用户名丢失，您是否确定要开启此功能？\n请再次输入 {code(f',{cmd_name} flood_username y')} 来确认"
    ],
    "flood_username_set": [
        f"Change username in flood preiod has been %s.",
        f"轰炸时切换用户名已%s"
    ],
    "flood_channel_desc": [
        ("This channel is a placeholder of username, which the owner is being flooded.\n"
         "Please content him later after this channel is gone."),
        "这是一个用于临时设置用户名的频道，该群主正在被私聊轰炸\n请在此频道消失后再联系他。"
    ],
    # Action
    "flood_act_curr_rule": [
        "Current flood action was set to %s",
        "当前轰炸操作已设置为 %s"
    ],
    "flood_act_set_asis": [
        f"All users in flood period will be {bold('treat as verify failed')}.",
        f"所有在轰炸期间的用户将会{bold('与验证失败的处理方式一致')}"
    ],
    "flood_act_set_captcha": [
        f"All users in flood period will be {bold('asked for captcha')}.",
        f"所有在轰炸期间的用户将会{bold('进行验证码挑战')}"
    ],
    "flood_act_set_none": [
        "Nothing will do to users in flood period.",
        "所有在轰炸期间的用户将不会被进行任何处理"
    ],
    "flood_act_set_delete": [
        "All flooded users will be deleted and reported spamming.",
        "所有轰炸的用户将会被举报并删除聊天"
    ],
    # endregion

    # region Custom Rule
    "custom_rule_curr_rule": [
        "Current custom rule",
        "当前自定义规则"
    ],
    "custom_rule_set": [
        f"Custom rule has been set to\n{code('%s')}.",
        f"已设置自定义规则为\n{code('%s')}"
    ],
    "custom_rule_reset": [
        "Custom rule has been deleted.",
        "已删除自定义规则"
    ],
    "custom_rule_exec_err": [
        "Error occurred when executing custom rule",
        "执行自定义规则时发生错误"
    ],
    # endregion

    # region Collect Logs
    "collect_logs_curr_rule": [
        "Current collect logs status: %s",
        "当前收集日志状态: 已%s"
    ],
    "collect_logs_note": [
        ("This feature will only collect user information and chat logs of non-verifiers "
         f"via @{log_collect_bot} , and is not provided to third parties (except @LivegramBot ).\n"
         "Information collected will be used for PMCaptcha improvements, "
         "toggling this feature does not affect the use of PMCaptcha."),
        (f"此功能仅会通过 @{log_collect_bot} 收集未通过验证者的用户信息以及验证未通过的聊天记录；"
         "且不会提供给第三方(@LivegramBot 除外)。\n收集的信息将用于 PMCaptcha 改进，开启或关闭此功能不影响 PMCaptcha 的使用。")
    ],
    "collect_logs_set": [
        "Collect logs has been set to %s.",
        "已设置收集日志为 %s"
    ],
    # endregion

    # region Captcha Type
    "type_curr_rule": [
        "Current captcha type: %s",
        "当前验证码类型: %s"
    ],
    "type_set": [
        f"Captcha type has been set to {bold('%s')}.",
        f"已设置验证码类型为 {bold('%s')}"
    ],
    "type_param_name": [
        "Type",
        "类型"
    ],
    "type_captcha_img": [
        "Image",
        "图像辨识"
    ],
    "type_captcha_math": [
        "Math",
        "计算"
    ],
    "type_captcha_sticker": [
        "Sticker",
        "贴纸"
    ],
    # endregion

    # region Image Captcha Type
    "img_captcha_curr_rule": [
        "Current image captcha type: %s",
        "当前图像验证类型: %s"
    ],
    "img_captcha_type_func": [
        "funCaptcha",
        "funCaptcha",
    ],
    "img_captcha_type_github": [
        "GitHub",
        "GitHub",
    ],
    "img_captcha_type_rec": [
        "reCaptcha",
        "reCaptcha"
    ],
    "img_captcha_retry_curr_rule": [
        "Current max retry for image captcha: %s",
        "当前图像验证码最大重试次数: %s"
    ],
    "img_captcha_retry_set": [
        "Max retry for image captcha has been set to %s.",
        "已设置图像验证码最大重试次数为 %s"
    ],
    # endregion
}
