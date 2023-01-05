import http from "./http"

export async function getAvailbleTheater() {
  return await http({
    method: "get",
    url: `/api/available_theaters/`,
  })
}

export async function getAvailableDate(theater_pk) {
  return await http({
    method: "get",
    url: `/api/available_date/${theater_pk}/`,
  })
}

export async function getAvailableMovie(theater_pk, date) {
  return await http({
    method: "get",
    url: `/api/available_movie/${theater_pk}/${date}/`,
  })
}

export async function getAvailableSchedule(theater_pk, date, movie_pk) {
  return await http({
    method: "get",
    url: `/api/available_schedule/${theater_pk}/${date}/${movie_pk}/`,
  })
}

export async function getAvailableSeatList(schedule_id) {
  return await http({
    method: "get",
    url: `/api/available_seats/${schedule_id}/`,
  })
}

export async function occupySeat(seat_id) {
  return await http({
    method: "post",
    url: `/api/seats/${seat_id}/occupy/`,
  })
}

export async function kakaopayReady(seats_no) {
  return await http({
    method: "post",
    url: `/api/kakaopay/ready/`,
    data: {
      seats_no,
    },
  })
}

export async function kakaopayCheckSuccess(uuid, pg_token) {
  return await http({
    method: "get",
    url: `/api/kakaopay/${uuid}/success/`,
    params: {
      pg_token,
    },
  })
}

export async function readTheaterItem(id) {
  return await http({
    method: "get",
    url: `/api/theaters/${id}/`,
  })
}
