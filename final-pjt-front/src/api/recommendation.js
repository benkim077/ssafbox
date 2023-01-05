import http from "./http"

export async function getRecommendedMovie() {
  return await http({
    method: "get",
    url: `/api/recommendation/`,
  })
}
