from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)
    invite_code_id = Column(Integer, ForeignKey("invite_codes.id"), nullable=True)
    taste_map = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

class InviteCode(Base):
    __tablename__ = "invite_codes"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
    is_used = Column(Boolean, default=False)
    created_for = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    location = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    is_vault = Column(Boolean, default=False)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

class VaultCollection(Base):
    __tablename__ = "vault_collections"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    property_ids = Column(Text)  # JSON string
    created_at = Column(DateTime, server_default=func.now())

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    request_type = Column(String)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=True)
    payload = Column(Text, nullable=True)
    status = Column(String, default="pending")
    created_at = Column(DateTime, server_default=func.now())
