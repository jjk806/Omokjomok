<template>
  <div class="post">
    <div class="wrapB">
      <h2>대전 방</h2>

      <section class="post-list">
        <div>
          <div class="post-card">
            <a>
              <div 
                :style="{ backgroundImage:'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',}"
                class="post-img"
              />
              <div class="contents">
                <h3>제목</h3>
                <p class="content">컨텐츠</p>
                <span class="date">2020-06-19ㆍ</span>
                <span class="comment">댓글 0개</span>
              </div>
            </a>

            <div class="writer-wrap">
              <a>닉네임</a>
              <span>♥ 2</span>
            </div>
          </div>
        </div>
        <div>
          <div class="post-card">
            <a>
              <div
                :style="{
                  backgroundImage:
                    'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',
                }"
                class="post-img"
              />

              <div class="contents">
                <h3>
                  제목
                </h3>
                <p class="content">컨텐츠</p>
                <span class="date">2020-06-19ㆍ</span>
                <span class="comment">댓글 0개</span>
              </div>
            </a>

            <div class="writer-wrap">
              <a>
                닉네임
              </a>
              <span>
                ♥ 2
              </span>
            </div>
          </div>
        </div>
        <div>
          <div class="post-card">
            <a>
              <div
                :style="{
                  backgroundImage:
                    'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',
                }"
                class="post-img"
              />

              <div class="contents">
                <h3>
                  제목
                </h3>
                <p class="content">컨텐츠</p>
                <span class="date">2020-06-19ㆍ</span>
                <span class="comment">댓글 0개</span>
              </div>
            </a>

            <div class="writer-wrap">
              <a>
                닉네임
              </a>
              <span>
                ♥ 2
              </span>
            </div>
          </div>
        </div>
        <div>
          <div class="post-card">
            <a>
              <div
                :style="{
                  backgroundImage:
                    'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',
                }"
                class="post-img"
              />

              <div class="contents">
                <h3>
                  제목
                </h3>
                <p class="content">컨텐츠</p>
                <span class="date">2020-06-19ㆍ</span>
                <span class="comment">댓글 0개</span>
              </div>
            </a>

            <div class="writer-wrap">
              <a>
                닉네임
              </a>
              <span>
                ♥ 2
              </span>
            </div>
          </div>
        </div>
        <div>
          <div class="post-card">
            <a>
              <div
                :style="{
                  backgroundImage:
                    'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',
                }"
                class="post-img"
              />

              <div class="contents">
                <h3>
                  제목
                </h3>
                <p class="content">컨텐츠</p>
                <span class="date">2020-06-19ㆍ</span>
                <span class="comment">댓글 0개</span>
              </div>
            </a>

            <div class="writer-wrap">
              <a>
                닉네임
              </a>
              <span>
                ♥ 2
              </span>
            </div>
          </div>
        </div>
        <div>
          <div class="post-card">
            <a>
              <div
                :style="{
                  backgroundImage:
                    'url(https://www.ipcc.ch/site/assets/uploads/sites/3/2019/10/img-placeholder.png)',
                }"
                class="post-img"
              />

              <div class="contents">
                <h3>
                  제목
                </h3>
                <p class="content">컨텐츠</p>
                <span class="date">2020-06-19ㆍ</span>
                <span class="comment">댓글 0개</span>
              </div>
            </a>

            <div class="writer-wrap">
              <a>
                닉네임
              </a>
              <span>
                ♥ 2
              </span>
            </div>
          </div>
        </div>
      </section>

      <div class="tag-list-wrap">
        <b-container>
          <b-row>
            <b-col>
              <h4>Rating</h4>
            </b-col>
          </b-row>
          <b-row>
            <b-col>No.</b-col>
            <b-col>Name</b-col>
            <b-col>승률</b-col>
          </b-row>
          <hr>
          <!-- 반복문 -->
          <b-row>
            <b-col>1</b-col>
            <b-col>싸피1</b-col>
            <b-col>100%</b-col>
          </b-row>
          <b-row>
            <b-col>2</b-col>
            <b-col>싸피2</b-col>
            <b-col>90%</b-col>
          </b-row>
          <b-row>
            <b-col>3</b-col>
            <b-col>싸피3</b-col>
            <b-col>80%</b-col>
          </b-row>
          <b-row>
            <b-col>4</b-col>
            <b-col>싸피4</b-col>
            <b-col>70%</b-col>
          </b-row>
          <b-row>
            <b-col>5</b-col>
            <b-col>싸피5</b-col>
            <b-col>60%</b-col>
          </b-row>
        </b-container>
      </div>
    </div>
  </div>
</template>

<script>
import "../../assets/css/post.scss";

export default {
  name: "Post",
  components: {},
  watch: {},
  created() {},
  methods: {},
  data: () => {
    return {};
  },
};
</script>
