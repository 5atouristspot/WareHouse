<template>
  <div id="plan" >
    <GoBack v-bind:target="target"/>
    <div class="content-div global-bg-color">
      <div class="button-line">
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '1')">高架库区</el-button>
        </div>
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '2')">高架库预留区</el-button>
        </div>
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '3')">地面库区1</el-button>
        </div>
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '4')">地面库区2</el-button>
        </div>
      </div>
      <div class="button-line">
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '5')">储存间</el-button>
        </div>
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '6')">低温-18℃冷库区</el-button>
        </div>
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '7')">恒温胶囊库区</el-button>
        </div>
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '8')">包材储存间</el-button>
        </div>
      </div>
      <div class="button-line">
        <div class="button-div">
          <!--<el-button type="primary" @click="redirect('batch', '1')">API-原料</el-button>-->
          <el-button type="primary" @click="redirect('warehouse', '11')">API-原料</el-button>
        </div>
        <div class="button-div">
          <!--<el-button type="primary" @click="redirect('batch', '2')">API-成品</el-button>-->
           <el-button type="primary" @click="redirect('warehouse', '12')">API-成品</el-button>
        </div>
        <div class="button-div">
          <!--<el-button type="primary" @click="redirect('batch', '3')">安全储存柜</el-button>-->
          <el-button type="primary" @click="redirect('warehouse', '13')">安全储存柜</el-button>
        </div>
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '9')">冰柜</el-button>
        </div>
        <div style="width: 0px">
        </div>
      </div>
      <div class="button-line">
        <div class="button-div">
          <el-button type="primary" @click="redirect('batch', '4')">VENDOR</el-button>
        </div>
        <div class="button-div">
          <el-button type="primary" @click="redirect('warehouse', '10')">高架库地面货位</el-button>
        </div>
      </div>
      <div class="refresh-div">
        <!--<div>
          <el-button type="danger" @click="refreshData()">刷新数据</el-button>
        </div>
        <div class="refresh-time-div" v-if="isShowTime">
          <div>上次刷新时间：</div>
          <div class="time-div">{{dateTime}}</div>
        </div>-->
        <div>
          <el-button type="danger" @click="goSupplier()">供应商备货管理</el-button>
          <el-button type="danger" @click="goSearch()">搜索</el-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import GoBack from '@/components/GoBack'
  export default {
    name: 'plan',

    data () {
      return {
        target: '/login',
        isShowTime: false,
        dateTime:''
      }
    },
    methods: {
      init(){
        if (window.localStorage) {
          let localStorage = window.localStorage;
          let refresh_datetime_cookie = localStorage.getItem("refresh_datetime_cookie")
          if (refresh_datetime_cookie) {
            this.showTime(refresh_datetime_cookie);
          }
        }
      },
      goSearch() {
        this.$router.push("/search")
      },
      goSupplier() {
        this.$router.push("/supplier")
      },
      redirect(path, type) {
        console.log("path:" + path + ",type:" + type)
        this.$router.push(`/${path}/${type}`)
      },
      showTime(dateTime) {
        this.isShowTime = true
        this.dateTime = dateTime
      },
      refreshData() {
        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.post('/api/v1000/elevated/reloaddata').then(res => {
          let data = res.data
          if (data && data.status === 0) {
            let dateTime = this.getDateTime()
            this.showTime(dateTime);
            if (window.localStorage) {
              let localStorage = window.localStorage;
              localStorage.setItem("refresh_datetime_cookie", dateTime);
            }
          }
        })
      },
      getDateTime() {
        let myDate = new Date();
        //获取当前年
        let year = myDate.getFullYear();
        //获取当前月
        let month = myDate.getMonth() + 1;
        //获取当前日
        let date = myDate.getDate();
        let h = myDate.getHours(); //获取当前小时数(0-23)
        let m = myDate.getMinutes(); //获取当前分钟数(0-59)
        let s = myDate.getSeconds();
        let now =
          year +
          "/" +
          this.getNow(month) +
          "/" +
          this.getNow(date) +
          " " +
          this.getNow(h) +
          ":" +
          this.getNow(m) +
          ":" +
          this.getNow(s);
        return now;
      },
      getNow(s) {
        return s < 10 ? "0" + s : s;
      }
    },
    components: {
      GoBack: GoBack
    },
    created() {
      this.init();
    }
  }
</script>

<style lang="less" scoped>

  .content-div {
    width: 100%;
    height: 100%;
    text-align: center;
    padding-top: 30px;
  }
  .button-line {
    display: flex;
    justify-content: center;
  }
  .button-div {
    margin: 5px;
  }

  .button-div button {
    width: 350px;
    height: 100px;
  }
  .refresh-div {
    width: 100%;
    margin-top: 100px;
  }
  .refresh-div button {
    width: 350px;
    height: 100px;
  }

  .refresh-time-div {
    margin-top: 10px;
    color: #000000;
    font-size: 24px;
    font-weight: 600;
  }
  .refresh-time-div div {
    display: inline-block;
  }
  .el-button--danger {
    color: #F8F8FF;
    font-size: 30px;
    background-color: #00b2b0;
    border-color: #00b2b0;
  }
  .el-button--danger:hover, .el-button--danger:focus {
    color: #F8F8FF;
    font-size: 30px;
    background-color: #00b2b0;
    border-color: #00b2b0;
  }

</style>
        
