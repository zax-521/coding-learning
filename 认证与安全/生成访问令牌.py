"""
    web中的Token：是服务器发给客户端的一段字符串，用来在后续请求中证明"你已经登录过了"

    作用：解决HTTP是无状态的问题，在每次请求中"自我证明身份"

    流程：
        登录或注册 → 后端生成 Token → 后端返回 Token → 前端保存 Token → 每次请求时携带 Token → 后端验证 Token

    Token在请求中的位置：请求头
        Authorization: Bearer <token>
        Authorization：专门用来放身份信息
        Bearer：表示"持有者令牌"
        <token>：身份凭证

    uuid 生成临时 Token
    token = str(uuid.uuid4())

"""