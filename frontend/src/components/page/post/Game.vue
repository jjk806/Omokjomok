<template>
  <div>
    <br><br>
    <h1>대국</h1>
    <br><br><br>
    <b-container fluid>
      <b-row>
        <!-- 대국 -->
        <b-col offset="1" cols="6">
          <img src="../../assets/omok_pan.png" height="800px" alt="">
        </b-col>
        <b-col cols="4">
          <!-- player1 -->
          <b-row class="pt-5 pb-2">
            <b-col>
              <img src="../../assets/user1.png" height="150px" alt="">
            </b-col>
            <b-col align-self="center">
              <b-progress :value="value" :max="max" class="mb-3"></b-progress>
              {{ value }}초
            </b-col>
          </b-row>
          <b-row class="pb-5">
            <b-col align-self="center">사용자1</b-col>
            <b-col >
              <img src="../../assets/black_doll.png" height="50px" alt="">
            </b-col>
          </b-row>
          <!-- VS -->
          <b-row class="py-5">
            <b-col offset="2" align-self="center"><b-button>무르기</b-button></b-col>
            <b-col align-self="center"><div class="round-btn">착수</div></b-col>
            <b-col align-self="center"><b-button>기권</b-button></b-col>
          </b-row>
          <!-- player2 -->
          <b-row class="pt-5 pb-2">
            <b-col>
              <img src="../../assets/user2.png" height="150px" alt="">
            </b-col>
            <b-col align-self="center">
              <b-progress :value="value" :max="max" class="mb-3"></b-progress>
              {{ value }}초
            </b-col>
          </b-row>
          <b-row class="pb-5">
            <b-col align-self="center">사용자2</b-col>
            <b-col>
              <img src="../../assets/white_doll.png" height="50px" alt="">
            </b-col>
          </b-row>
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
        max: 30
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