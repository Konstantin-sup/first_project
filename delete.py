def del_from_db(session, id: int):
    """No commit, so i don't accidentally delete some data(even from test base)"""
    user = session.get(User, id)  #getting user with target id from 'User' base(Model)
    user_protected = session.get(Protected, id)  #same operation but from 'Protected' base(Model)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="id doesn't exist"
        )

    session.delete(user)
    session.delete(user_protected)
    session.flush()
