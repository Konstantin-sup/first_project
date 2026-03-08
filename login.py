def select_data_login(session_factory, us_name):
    with session_factory as session:
        req = select(Protected).where(
            Protected.user_name == us_name
        )
        res = session.execute(req)
        users = res.scalars().all()
        return users
