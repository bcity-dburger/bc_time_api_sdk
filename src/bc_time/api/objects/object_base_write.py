from bc_time.api.objects.object_base_create import ObjectBaseCreate
from bc_time.api.objects.object_base_update import ObjectBaseUpdate
from bc_time.api.constants.api import Api as ApiConstants

class ObjectBaseWrite(ObjectBaseUpdate, ObjectBaseUpdate):
    def create(self, payload: dict) -> dict:
        return self.api.create(
            content_type_id=self._content_type_id,
            payload=payload
        )

    def create_many(self, payloads: dict) -> dict:
        return self.api.create(
            content_type_id=self._content_type_id,
            payloads=payloads,
            content_uid=ApiConstants.UID_POST_MANY
        )

    def update(self, content_uid, payload: dict) -> dict:
        return self.api.update(
            content_type_id=self._content_type_id,
            content_uid=content_uid,
            payload=payload
        )

    def update_many(self, payloads: dict) -> dict:
        return self.api.update(
            content_type_id=self._content_type_id,
            content_uid=ApiConstants.UID_POST_MANY,
            payload=payloads
        )