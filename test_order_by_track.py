# Александр Сотников, 38-я когорта — Финальный проект. Инженер по тестированию плюс

from http import HTTPStatus
import data
import sender_stand_request as stand


def test_created_order_returns_track():
    resp = stand.create_order(data.order_body)
    body = resp.json()

    assert resp.status_code == HTTPStatus.CREATED
    assert body.get("track") is not None


def test_get_order_by_track_200():
    resp = stand.create_order(data.order_body)
    body = resp.json()
    track = body.get("track")
    get_response = stand.get_order_by_track(track)

    assert get_response.status_code == HTTPStatus.OK
