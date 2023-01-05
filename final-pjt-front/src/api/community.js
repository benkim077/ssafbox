import http from "./http"

export async function getReviewList(movie_id) {
  return await http({
    method: "get",
    url: `/api/reviews/`,
    params: {
      movie_id,
    },
  })
}

export async function createReview(movie_id, content) {
  return await http({
    method: "post",
    url: `/api/reviews/`,
    data: {
      movie_id,
      content,
    },
  })
}

export async function deleteReview(review_id) {
  return await http({
    method: "delete",
    url: `/api/reviews/${review_id}/`,
  })
}
