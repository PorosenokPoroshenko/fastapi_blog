from sqlalchemy.orm import Session

from . import models, schemas


def get_post(db: Session, post_id: int) -> models.Post:
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_latest_post(db: Session) -> models.Post:
    # order posts by date in descending order, get the first one(the latest)
    return db.query(models.Post).order_by(models.Post.date.desc()).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100) -> models.Post:
    # skips {skip} posts and returns up to {limit} of them
    return (
        db.query(models.Post)
        .order_by(models.Post.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_post(db: Session, post: schemas.PostCreate) -> models.Post:
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
