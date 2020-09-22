<template>
  <div>
    <br><br>
    <h1>최근 대국</h1>
    <br><br><br>
    <b-container fluid>
      <b-row>
        <!-- 대국 -->
        <b-col>
          <img src="../../assets/omok_pan.png" height="800px" alt="">
        </b-col>
      </b-row>
      <b-row class="my-5">
        <b-col>
          <!-- Use text in props -->
          <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="1"
            first-text="First"
            prev-text="Prev"
            next-text="Next"
            last-text="Last"
            align="center"
            size="lg"
          ></b-pagination>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
    data() {
      return {
        value: 10,
        max: 30,
        // 기보 총 오목돌을 놓은 수
        rows: 100,
        perPage: 10,
        currentPage: 1
      }
    },

}
</script>

<style>
.round-btn {
  margin: 0 auto;
  display:block;
  width:80px;
  height:80px;
  line-height:70px;
  border: 5px solid #f5f5f5;
  border-radius: 50%;
  color:#f5f5f5;
  text-align:center;
  background-color: #1e292c;
  font-size:20px;
  font-weight:bold;
  text-decoration: none;
}
.round-btn:hover {
  color: #030303;
  background-color: #978989;
  text-decoration: none;
  cursor: pointer;
}
</style>