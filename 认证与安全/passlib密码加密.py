"""
    passlib 密码加密步骤：
        1.安装 passlib
            pip install passlib[bcrypt]==1.7.4
        2.创建加密上下文
            pwd_context = CryptContext(
                schemes=["bcrypt"],
                deprecated="auto",
            )
        3.加密或校验
            加密：pwd_context.hash(password)
            校验：pwd_context.verify(plain_password, hashed_password)
"""