<template>
  <b-container>
    <br><br>
    <div class="mt-5">
      <b-row>
        <b-col cols="4" id="mypageImage">
          <b-row>
            <b-col>
              <b-img
                id="myimg"
                :src="defaultImageUrl"
                width="300"
                height="300"
                rounded="circle"
                alt="프로필 이미지"
              ></b-img>
            </b-col>
          </b-row>
          <br>
          <b-row>
            <b-col>
              <b-button variant="primary" class="btn_upload" type="button">이미지 업로드</b-button>
              <input 
                id="refresh"
                type="file"
                value="upload"
                style="display: none;"
                ref="fileInput"
                accept="image/*"
              />
            </b-col>
          </b-row>
        </b-col>
        <b-col cols="8" id="mypageInfo">
          <div id="userInfoList">
            <b-row>
              <b-col md="3" offset-md="1" class="text-left font-weight-bold">이메일</b-col>
              <b-col md="3" offset-md="3" class="text-right font-weight-bold">ssafy@ssafy.com</b-col>
            </b-row>
            <hr>
            <b-row>
              <b-col md="3" offset-md="1" class="text-left font-weight-bold">이름</b-col>
              <b-col md="3" offset-md="3" class="text-right font-weight-bold">ssafy1</b-col>
            </b-row>
            <hr>
            <b-row>
              <b-col md="3" offset-md="1" class="text-left font-weight-bold">승률</b-col>
              <b-col md="3" offset-md="3" class="text-right font-weight-bold">100%</b-col>
            </b-row>
            <hr>
          </div>
          <div id="mypageBtn">
            <b-row align-h="end" class="text-right">
              <div class="badge text-wrap mr-2" style="width: 9rem;">
                <b-button route :to="{ name: 'UpdateUserInfo' }" variant="warning">회원정보 수정</b-button>
              </div>
              <div class="badge text-wrap mr-2" style="width: 9rem;">
                <b-button route :to="{ name: 'EditPassword' }" variant="success">비밀번호 변경</b-button>
              </div>
              <div class="badge text-wrap mr-2" style="width: 7rem;">
                <b-button variant="danger" v-b-modal.my-modal>회원탈퇴</b-button>
              </div>
            </b-row>
          </div>
        </b-col>
      </b-row>
      <hr />
      <div>
        <b-tabs content-class="mt-3" justified>
          <b-tab title="최근 대국" active>
            <p>최근 대국</p>
            <b-row>
              <b-col cols="4" class="recentGame border p-0">
                <a>
                  <div
                    :style="{
                      backgroundImage:
                        'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',
                    }"
                    class="post-img"
                  />

                  <div class="contents">
                    <h3>제목</h3>
                    <p class="content">컨텐츠</p>
                    <span class="date">2020-06-19ㆍ</span>
                    <span class="comment">댓글 0개</span>
                  </div>
                </a>
              </b-col>
              <b-col cols="4" class="recentGame border p-0">
                <a>
                  <div
                    :style="{
                      backgroundImage:
                        'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',
                    }"
                    class="post-img"
                  />

                  <div class="contents">
                    <h3>제목</h3>
                    <p class="content">컨텐츠</p>
                    <span class="date">2020-06-19ㆍ</span>
                    <span class="comment">댓글 0개</span>
                  </div>
                </a>
              </b-col>
              <b-col cols="4" class="recentGame border p-0">
                <a>
                  <div
                    :style="{
                      backgroundImage:
                        'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',
                    }"
                    class="post-img"
                  />

                  <div class="contents">
                    <h3>제목</h3>
                    <p class="content">컨텐츠</p>
                    <span class="date">2020-06-19ㆍ</span>
                    <span class="comment">댓글 0개</span>
                  </div>
                </a>
              </b-col>
            </b-row>
            <br />
            <b-row>
              <b-col>
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="my-table"
                  align="center"
                ></b-pagination>
              </b-col>
            </b-row>
          </b-tab>
          <b-tab title="승률">
            <p>승률</p>
            <router-link to="/chartjs">vue-chartjs</router-link>
          </b-tab>
        </b-tabs>
      </div>
    </div>
  </b-container>
</template>

<script>
export default {
  name: "Mypage",
  data() {
    return {
      defaultImageUrl:
        "https://previews.123rf.com/images/salamatik/salamatik1801/salamatik180100019/92979836-%ED%94%84%EB%A1%9C%ED%95%84-%EC%9D%B5%EB%AA%85%EC%9D%98-%EC%96%BC%EA%B5%B4-%EC%95%84%EC%9D%B4%EC%BD%98-%ED%9A%8C%EC%83%89-%EC%8B%A4%EB%A3%A8%EC%97%A3-%EC%82%AC%EB%9E%8C%EC%9E%85%EB%8B%88%EB%8B%A4-%EB%82%A8%EC%84%B1-%EA%B8%B0%EB%B3%B8-%EC%95%84%EB%B0%94%ED%83%80-%EC%82%AC%EC%A7%84-%EC%9E%90%EB%A6%AC-%ED%91%9C%EC%8B%9C-%EC%9E%90-%ED%9D%B0%EC%83%89-%EB%B0%B0%EA%B2%BD%EC%97%90-%EA%B3%A0%EB%A6%BD-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EB%A0%88%EC%9D%B4-%EC%85%98.jpg",

      perPage: 3,
      currentPage: 1,
      items: [
        { id: 1, first_name: "Fred", last_name: "Flintstone" },
        { id: 2, first_name: "Wilma", last_name: "Flintstone" },
        { id: 3, first_name: "Barney", last_name: "Rubble" },
        { id: 4, first_name: "Betty", last_name: "Rubble" },
        { id: 5, first_name: "Pebbles", last_name: "Flintstone" },
        { id: 6, first_name: "Bamm Bamm", last_name: "Rubble" },
        { id: 7, first_name: "The Great", last_name: "Gazzoo" },
        { id: 8, first_name: "Rockhead", last_name: "Slate" },
        { id: 9, first_name: "Pearl", last_name: "Slaghoople" },
      ],
    };
  },
  computed: {
    rows() {
      return this.items.length;
    },
  },
  methods: {},
};
</script>

<style>
.post-img {
  height: 300px;
}
</style>
