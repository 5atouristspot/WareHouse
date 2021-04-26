<template>
  <div id="warehouse global-bg-color">
    <GoBack v-bind:target="target"/>
    <div class="top-div global-bg-color">
      <el-row style="width: 100%">
        <el-col :span="(index > 0 && index == utilizationRateList.length - 1) ? 6 : 3" v-for="(item, index) in utilizationRateList" :key="index">
          <el-row v-if="subIndex !== 'class'" v-for="(subItem, subIndex) in item.list" :key="subIndex" class="item-row">
            <el-col :span="14" class="subItem-left-col"><div>{{subIndex}}</div></el-col>
            <el-col :span="10" class="subItem-right-col"><div :class="subIndex === specialKey ? item.list['class'] : ''">{{item.list[subIndex]}}</div></el-col>
          </el-row>
        </el-col>
      </el-row>
    </div>

    <div v-if="type === '1'">
      <div class="special-content-div global-bg-color tl">
        <el-row v-for="(item, index) in storagebinList" :key="index" class="storage-col">
          <el-col class="storage-left-col">{{item.name}}</el-col>
          <el-col class="storage-right-col">
          <span v-for="(subItem, subIndex) in item.list" :key="subIndex">
            <br v-if="isShowBr(item, subIndex)">
            <div class="div-null" v-if="isShowNullDiv(item, subIndex)"></div>
            <el-button class="storage-item-btn"
                       :class="btnClass(subItem.status)"
                       @click="redirect(subItem.name, subItem.status)">
              {{subItem.name}}
            </el-button>
          </span>
          </el-col>
        </el-row>
      </div>
    </div>
    <div v-else>
      <div class="content-div global-bg-color tl">
        <el-row style="width: 100%" :gutter="10">
          <el-col :span="4" v-for="(item, index) in storagebinList" :key="index" style="margin-bottom: 10px">
            <el-button class="storagebin-btn"
                       :class="btnClass(item.status)"
                       @click="redirect(item.name, item.status)">
              {{item.name}}
            </el-button>
          </el-col>
        </el-row>
      </div>
    </div>

  </div>
</template>

<script>
  import GoBack from '@/components/GoBack'
  export default {
    name: 'warehouse',
    data() {
      return {
        target: '/plan',
        utilizationRateList: [],
        storagebinList: [],
        type: '',
        specialKey: '使用率',
        specialArray: ['02-05', '02-04', '02-03', '03-05', '03-04', '03-03', '05-05', '05-04', '05-03']
      }
    },
    methods: {
      init() {
        this.type = this.$route.params.type
        let reqParams = {
          warehouse_type: this.type
        }
        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.get('/api/v1000/elevated/utilization_rate', {params : reqParams}).then(res => {
          let data = res.data
          if (data && data.length > 0) {
            data.forEach((item, index) => {
              let list = item.list
              for (let key in list) {
                let value = list[key];
                let specialClass = ''
                if (key === this.specialKey) {
                  let pValue = (value*100).toPrecision(12);
                  pValue = parseFloat(pValue).toFixed(2);
                  if (pValue >= 50 && pValue < 80) {
                    specialClass = 'yellow'
                  } else if (pValue >= 80) {
                    specialClass = 'red'
                  } else {
                    specialClass = 'green'
                  }
                  value = pValue + '%';
                  list[key] = value
                }
                list['class'] = specialClass
                data[index] = item
              }
            })
            this.utilizationRateList = data
          }
        })

        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.get('/api/v1000/elevated/storagebin', {params : reqParams}).then(res => {
          let data = res.data
          // console.log("storagebin:" + JSON.stringify(data))
          if (data && data.length > 0) {
            if (this.type === '1') {
              data.forEach((item, index) => {
                let list = item.list;
                list.sort(this.sortBy('name'));
              })
            }
            this.storagebinList = data
          }
        })
        /*let data = [{"name": "\u4e00\u53f7\u8d27\u67b6", "list": [{"name": "01-02-01", "status": "\u5f85\u68c0"}, {"name": "01-02-02", "status": "\u5f85\u68c0"}, {"name": "01-02-03", "status": "\u5f85\u68c0"}, {"name": "01-02-04", "status": "\u5f85\u68c0"}, {"name": "01-02-05", "status": null}, {"name": "01-02-06", "status": null}, {"name": "01-03-01", "status": null}, {"name": "01-03-02", "status": "\u5f85\u68c0"}, {"name": "01-03-03", "status": null}, {"name": "01-03-04", "status": "\u5f85\u68c0"}, {"name": "01-03-05", "status": null}, {"name": "01-03-06", "status": null}, {"name": "01-04-01", "status": null}, {"name": "01-04-02", "status": "\u5f85\u68c0"}, {"name": "01-04-03", "status": null}, {"name": "01-04-04", "status": "\u5f85\u68c0"}, {"name": "01-04-05", "status": null}, {"name": "01-04-06", "status": null}, {"name": "01-05-01", "status": "\u5f85\u68c0"}, {"name": "01-05-02", "status": "\u5f85\u68c0"}, {"name": "01-05-03", "status": "\u5f85\u68c0"}, {"name": "01-05-04", "status": "\u5f85\u68c0"}, {"name": "01-05-05", "status": null}, {"name": "01-05-06", "status": null}, {"name": "01-06-01", "status": "\u5f85\u68c0"}, {"name": "01-06-02", "status": "\u5f85\u68c0"}, {"name": "01-06-03", "status": "\u5f85\u68c0"}, {"name": "01-06-04", "status": "\u5f85\u68c0"}, {"name": "01-06-05", "status": null}, {"name": "01-06-06", "status": null}, {"name": "01-07-01", "status": "\u5f85\u68c0"}, {"name": "01-07-02", "status": "\u5f85\u68c0"}, {"name": "01-07-03", "status": "\u5f85\u68c0"}, {"name": "01-07-04", "status": "\u5f85\u68c0"}, {"name": "01-07-05", "status": null}, {"name": "01-07-06", "status": null}, {"name": "01-08-01", "status": "\u5f85\u68c0"}, {"name": "01-08-02", "status": "\u5f85\u68c0"}, {"name": "01-08-03", "status": "\u5f85\u68c0"}, {"name": "01-08-04", "status": "\u5f85\u68c0"}, {"name": "01-08-05", "status": null}, {"name": "01-08-06", "status": null}, {"name": "01-09-01", "status": "\u5f85\u68c0"}, {"name": "01-09-02", "status": "\u5f85\u68c0"}, {"name": "01-09-03", "status": "\u5f85\u68c0"}, {"name": "01-09-04", "status": "\u5f85\u68c0"}, {"name": "01-09-05", "status": null}, {"name": "01-09-06", "status": null}, {"name": "01-10-01", "status": "\u5f85\u68c0"}, {"name": "01-10-02", "status": "\u5f85\u68c0"}, {"name": "01-10-03", "status": ""}, {"name": "01-10-04", "status": ""}, {"name": "01-10-05", "status": null}, {"name": "01-10-06", "status": null}, {"name": "01-11-01", "status": ""}, {"name": "01-11-02", "status": ""}, {"name": "01-11-03", "status": ""}, {"name": "01-11-04", "status": ""}, {"name": "01-11-05", "status": null}, {"name": "01-11-06", "status": null}, {"name": "01-12-01", "status": ""}, {"name": "01-12-02", "status": ""}, {"name": "01-12-03", "status": ""}, {"name": "01-12-04", "status": ""}, {"name": "01-12-05", "status": null}, {"name": "01-12-06", "status": null}, {"name": "01-13-01", "status": "\u5f85\u68c0"}, {"name": "01-13-02", "status": "\u5f85\u68c0"}, {"name": "01-13-03", "status": "\u5f85\u68c0"}, {"name": "01-13-04", "status": "\u5f85\u68c0"}, {"name": "01-13-05", "status": null}, {"name": "01-13-06", "status": null}, {"name": "01-14-01", "status": "\u5f85\u68c0"}, {"name": "01-14-02", "status": "\u5f85\u68c0"}, {"name": "01-14-03", "status": "\u5f85\u68c0"}, {"name": "01-14-04", "status": "\u5f85\u68c0"}, {"name": "01-14-05", "status": null}, {"name": "01-14-06", "status": null}, {"name": "01-15-01", "status": ""}, {"name": "01-15-02", "status": ""}, {"name": "01-15-03", "status": null}, {"name": "01-15-04", "status": "\u5f85\u68c0"}, {"name": "01-15-05", "status": null}, {"name": "01-15-06", "status": null}, {"name": "01-16-01", "status": ""}, {"name": "01-16-02", "status": ""}, {"name": "01-16-03", "status": null}, {"name": "01-16-04", "status": "\u5f85\u68c0"}, {"name": "01-16-05", "status": null}, {"name": "01-16-06", "status": null}, {"name": "01-17-01", "status": ""}, {"name": "01-17-02", "status": ""}, {"name": "01-17-03", "status": ""}, {"name": "01-17-04", "status": "\u5f85\u68c0"}, {"name": "01-17-05", "status": null}, {"name": "01-17-06", "status": null}, {"name": "01-18-01", "status": "\u5f85\u68c0"}, {"name": "01-18-02", "status": "\u5f85\u68c0"}, {"name": "01-18-03", "status": "\u5f85\u68c0"}, {"name": "01-18-04", "status": "\u5f85\u68c0"}, {"name": "01-18-05", "status": null}, {"name": "01-18-06", "status": null}, {"name": "01-19-01", "status": "\u5f85\u68c0"}, {"name": "01-19-02", "status": "\u5f85\u68c0"}, {"name": "01-19-03", "status": "\u5f85\u68c0"}, {"name": "01-19-04", "status": "\u5f85\u68c0"}, {"name": "01-19-05", "status": null}, {"name": "01-19-06", "status": null}, {"name": "01-20-01", "status": "\u5f85\u68c0"}, {"name": "01-20-02", "status": "\u5f85\u68c0"}, {"name": "01-20-03", "status": "\u5f85\u68c0"}, {"name": "01-20-04", "status": "\u5f85\u68c0"}, {"name": "01-20-05", "status": null}, {"name": "01-20-06", "status": null}, {"name": "01-21-01", "status": ""}, {"name": "01-21-02", "status": ""}, {"name": "01-21-03", "status": "\u5f85\u68c0"}, {"name": "01-21-04", "status": "\u5f85\u68c0"}, {"name": "01-21-05", "status": null}, {"name": "01-21-06", "status": null}, {"name": "01-22-01", "status": ""}, {"name": "01-22-02", "status": ""}, {"name": "01-22-03", "status": "\u5f85\u68c0"}, {"name": "01-22-04", "status": "\u5f85\u68c0"}, {"name": "01-22-05", "status": null}, {"name": "01-22-06", "status": null}, {"name": "01-23-01", "status": "\u5f85\u68c0"}, {"name": "01-23-02", "status": "\u5f85\u68c0"}, {"name": "01-23-03", "status": "\u5f85\u68c0"}, {"name": "01-23-04", "status": "\u5f85\u68c0"}, {"name": "01-23-05", "status": null}, {"name": "01-23-06", "status": null}, {"name": "01-24-01", "status": "\u5f85\u68c0"}, {"name": "01-24-02", "status": "\u5f85\u68c0"}, {"name": "01-24-03", "status": "\u5f85\u68c0"}, {"name": "01-24-04", "status": null}, {"name": "01-24-05", "status": null}, {"name": "01-24-06", "status": null}, {"name": "01-25-01", "status": "\u5f85\u68c0"}, {"name": "01-25-02", "status": "\u5f85\u68c0"}, {"name": "01-25-03", "status": "\u5f85\u68c0"}, {"name": "01-25-04", "status": "\u5f85\u68c0"}, {"name": "01-25-05", "status": null}, {"name": "01-25-06", "status": null}, {"name": "01-26-01", "status": "\u5f85\u68c0"}, {"name": "01-26-02", "status": "\u5f85\u68c0"}, {"name": "01-26-03", "status": "\u5f85\u68c0"}, {"name": "01-26-04", "status": "\u5f85\u68c0"}, {"name": "01-26-05", "status": null}, {"name": "01-26-06", "status": null}, {"name": "01-27-01", "status": "\u5f85\u68c0"}, {"name": "01-27-02", "status": null}, {"name": "01-27-03", "status": "\u5f85\u68c0"}, {"name": "01-27-04", "status": "\u5f85\u68c0"}, {"name": "01-27-05", "status": null}, {"name": "01-27-06", "status": null}, {"name": "01-28-01", "status": "\u5f85\u68c0"}, {"name": "01-28-02", "status": "\u5f85\u68c0"}, {"name": "01-28-03", "status": "\u5f85\u68c0"}, {"name": "01-28-04", "status": "\u5f85\u68c0"}, {"name": "01-28-05", "status": null}, {"name": "01-28-06", "status": null}, {"name": "01-29-01", "status": "\u5f85\u68c0"}, {"name": "01-29-02", "status": "\u5f85\u68c0"}, {"name": "01-29-03", "status": "\u5f85\u68c0"}, {"name": "01-29-04", "status": "\u5f85\u68c0"}, {"name": "01-29-05", "status": null}, {"name": "01-29-06", "status": null}, {"name": "01-30-01", "status": null}, {"name": "01-30-02", "status": "\u5f85\u68c0"}, {"name": "01-30-03", "status": "\u5f85\u68c0"}, {"name": "01-30-04", "status": "\u5f85\u68c0"}, {"name": "01-30-05", "status": null}, {"name": "01-30-06", "status": null}, {"name": "01-31-01", "status": null}, {"name": "01-31-02", "status": "\u5f85\u68c0"}, {"name": "01-31-03", "status": "\u5f85\u68c0"}, {"name": "01-31-04", "status": "\u5f85\u68c0"}, {"name": "01-31-05", "status": null}, {"name": "01-31-06", "status": null}, {"name": "01-32-01", "status": ""}, {"name": "01-32-02", "status": ""}, {"name": "01-32-03", "status": null}, {"name": "01-32-04", "status": null}, {"name": "01-32-05", "status": null}, {"name": "01-32-06", "status": null}]}, {"name": "\u4e8c\u53f7\u8d27\u67b6", "list": [{"name": "02-01-03", "status": null}, {"name": "02-01-04", "status": null}, {"name": "02-01-05", "status": null}, {"name": "02-02-01", "status": ""}, {"name": "02-02-02", "status": "\u5f85\u68c0"}, {"name": "02-02-03", "status": ""}, {"name": "02-02-04", "status": null}, {"name": "02-02-05", "status": ""}, {"name": "02-02-06", "status": ""}, {"name": "02-03-01", "status": ""}, {"name": "02-03-02", "status": "\u5f85\u68c0"}, {"name": "02-03-03", "status": ""}, {"name": "02-03-04", "status": null}, {"name": "02-03-05", "status": ""}, {"name": "02-03-06", "status": ""}, {"name": "02-04-01", "status": ""}, {"name": "02-04-02", "status": "\u5f85\u68c0"}, {"name": "02-04-03", "status": ""}, {"name": "02-04-04", "status": null}, {"name": "02-04-05", "status": ""}, {"name": "02-04-06", "status": ""}, {"name": "02-05-01", "status": ""}, {"name": "02-05-02", "status": "\u5f85\u68c0"}, {"name": "02-05-03", "status": ""}, {"name": "02-05-04", "status": null}, {"name": "02-05-05", "status": ""}, {"name": "02-05-06", "status": ""}, {"name": "02-06-01", "status": "\u5f85\u68c0"}, {"name": "02-06-02", "status": "\u5f85\u68c0"}, {"name": "02-06-03", "status": ""}, {"name": "02-06-04", "status": null}, {"name": "02-06-05", "status": ""}, {"name": "02-06-06", "status": ""}, {"name": "02-07-01", "status": "\u5f85\u68c0"}, {"name": "02-07-02", "status": "\u5f85\u68c0"}, {"name": "02-07-03", "status": ""}, {"name": "02-07-04", "status": null}, {"name": "02-07-05", "status": ""}, {"name": "02-07-06", "status": ""}, {"name": "02-08-01", "status": "\u5f85\u68c0"}, {"name": "02-08-02", "status": "\u5f85\u68c0"}, {"name": "02-08-03", "status": ""}, {"name": "02-08-04", "status": null}, {"name": "02-08-05", "status": ""}, {"name": "02-08-06", "status": ""}, {"name": "02-09-01", "status": "\u5f85\u68c0"}, {"name": "02-09-02", "status": "\u5f85\u68c0"}, {"name": "02-09-03", "status": ""}, {"name": "02-09-04", "status": null}, {"name": "02-09-05", "status": ""}, {"name": "02-09-06", "status": ""}, {"name": "02-10-01", "status": "\u5f85\u68c0"}, {"name": "02-10-02", "status": "\u5f85\u68c0"}, {"name": "02-10-03", "status": ""}, {"name": "02-10-04", "status": null}, {"name": "02-10-05", "status": ""}, {"name": "02-10-06", "status": ""}, {"name": "02-11-01", "status": "\u5f85\u68c0"}, {"name": "02-11-02", "status": "\u5f85\u68c0"}, {"name": "02-11-03", "status": ""}, {"name": "02-11-04", "status": null}, {"name": "02-11-05", "status": ""}, {"name": "02-11-06", "status": null}, {"name": "02-12-01", "status": "\u5f85\u68c0"}, {"name": "02-12-02", "status": null}, {"name": "02-12-03", "status": ""}, {"name": "02-12-04", "status": null}, {"name": "02-12-05", "status": ""}, {"name": "02-12-06", "status": ""}, {"name": "02-13-01", "status": "\u5f85\u68c0"}, {"name": "02-13-02", "status": null}, {"name": "02-13-03", "status": ""}, {"name": "02-13-04", "status": null}, {"name": "02-13-05", "status": ""}, {"name": "02-13-06", "status": ""}, {"name": "02-14-01", "status": "\u5f85\u68c0"}, {"name": "02-14-02", "status": null}, {"name": "02-14-03", "status": ""}, {"name": "02-14-04", "status": null}, {"name": "02-14-05", "status": ""}, {"name": "02-14-06", "status": ""}, {"name": "02-15-01", "status": "\u5f85\u68c0"}, {"name": "02-15-02", "status": null}, {"name": "02-15-03", "status": ""}, {"name": "02-15-04", "status": null}, {"name": "02-15-05", "status": ""}, {"name": "02-15-06", "status": null}, {"name": "02-16-01", "status": "\u5f85\u68c0"}, {"name": "02-16-02", "status": ""}, {"name": "02-16-03", "status": ""}, {"name": "02-16-04", "status": null}, {"name": "02-16-05", "status": ""}, {"name": "02-16-06", "status": ""}, {"name": "02-17-01", "status": "\u5f85\u68c0"}, {"name": "02-17-02", "status": ""}, {"name": "02-17-03", "status": ""}, {"name": "02-17-04", "status": null}, {"name": "02-17-05", "status": ""}, {"name": "02-17-06", "status": ""}, {"name": "02-18-01", "status": "\u5f85\u68c0"}, {"name": "02-18-02", "status": ""}, {"name": "02-18-03", "status": ""}, {"name": "02-18-04", "status": null}, {"name": "02-18-05", "status": ""}, {"name": "02-18-06", "status": null}, {"name": "02-19-01", "status": "\u5f85\u68c0"}, {"name": "02-19-02", "status": ""}, {"name": "02-19-03", "status": ""}, {"name": "02-19-04", "status": null}, {"name": "02-19-05", "status": ""}, {"name": "02-19-06", "status": null}, {"name": "02-20-01", "status": "\u5f85\u68c0"}, {"name": "02-20-02", "status": ""}, {"name": "02-20-03", "status": ""}, {"name": "02-20-04", "status": null}, {"name": "02-20-05", "status": ""}, {"name": "02-20-06", "status": null}, {"name": "02-21-01", "status": null}, {"name": "02-21-02", "status": ""}, {"name": "02-21-03", "status": ""}, {"name": "02-21-04", "status": null}, {"name": "02-21-05", "status": ""}, {"name": "02-21-06", "status": null}, {"name": "02-22-01", "status": null}, {"name": "02-22-02", "status": ""}, {"name": "02-22-03", "status": ""}, {"name": "02-22-04", "status": null}, {"name": "02-22-05", "status": ""}, {"name": "02-22-06", "status": null}, {"name": "02-23-01", "status": null}, {"name": "02-23-02", "status": ""}, {"name": "02-23-03", "status": ""}, {"name": "02-23-04", "status": null}, {"name": "02-23-05", "status": ""}, {"name": "02-23-06", "status": null}, {"name": "02-24-01", "status": null}, {"name": "02-24-02", "status": ""}, {"name": "02-24-03", "status": ""}, {"name": "02-24-04", "status": null}, {"name": "02-24-05", "status": ""}, {"name": "02-24-06", "status": null}, {"name": "02-25-01", "status": null}, {"name": "02-25-02", "status": ""}, {"name": "02-25-03", "status": ""}, {"name": "02-25-04", "status": null}, {"name": "02-25-05", "status": ""}, {"name": "02-25-06", "status": null}, {"name": "02-26-01", "status": null}, {"name": "02-26-02", "status": ""}, {"name": "02-26-03", "status": ""}, {"name": "02-26-04", "status": null}, {"name": "02-26-05", "status": ""}, {"name": "02-26-06", "status": null}, {"name": "02-27-01", "status": null}, {"name": "02-27-02", "status": ""}, {"name": "02-27-03", "status": ""}, {"name": "02-27-04", "status": null}, {"name": "02-27-05", "status": ""}, {"name": "02-27-06", "status": null}, {"name": "02-28-01", "status": null}, {"name": "02-28-02", "status": ""}, {"name": "02-28-03", "status": ""}, {"name": "02-28-04", "status": null}, {"name": "02-28-05", "status": ""}, {"name": "02-28-06", "status": null}, {"name": "02-29-01", "status": null}, {"name": "02-29-02", "status": ""}, {"name": "02-29-03", "status": ""}, {"name": "02-29-04", "status": null}, {"name": "02-29-05", "status": ""}, {"name": "02-29-06", "status": null}, {"name": "02-30-01", "status": null}, {"name": "02-30-02", "status": null}, {"name": "02-30-03", "status": ""}, {"name": "02-30-04", "status": null}, {"name": "02-30-05", "status": ""}, {"name": "02-30-06", "status": null}, {"name": "02-31-01", "status": null}, {"name": "02-31-02", "status": null}, {"name": "02-31-03", "status": ""}, {"name": "02-31-04", "status": null}, {"name": "02-31-05", "status": ""}, {"name": "02-31-06", "status": null}, {"name": "02-32-01", "status": null}, {"name": "02-32-02", "status": null}, {"name": "02-32-03", "status": ""}, {"name": "02-32-04", "status": null}, {"name": "02-32-05", "status": null}, {"name": "02-32-06", "status": null}]}, {"name": "\u4e09\u53f7\u8d27\u67b6", "list": [{"name": "03-01-03", "status": null}, {"name": "03-01-04", "status": null}, {"name": "03-01-05", "status": null}, {"name": "03-02-01", "status": null}, {"name": "03-02-02", "status": ""}, {"name": "03-02-03", "status": null}, {"name": "03-02-04", "status": null}, {"name": "03-02-05", "status": null}, {"name": "03-02-06", "status": null}, {"name": "03-03-01", "status": null}, {"name": "03-03-02", "status": ""}, {"name": "03-03-03", "status": null}, {"name": "03-03-04", "status": null}, {"name": "03-03-05", "status": null}, {"name": "03-03-06", "status": null}, {"name": "03-04-01", "status": ""}, {"name": "03-04-02", "status": ""}, {"name": "03-04-03", "status": null}, {"name": "03-04-04", "status": null}, {"name": "03-04-05", "status": null}, {"name": "03-04-06", "status": null}, {"name": "03-05-01", "status": ""}, {"name": "03-05-02", "status": ""}, {"name": "03-05-03", "status": null}, {"name": "03-05-04", "status": null}, {"name": "03-05-05", "status": null}, {"name": "03-05-06", "status": null}, {"name": "03-06-01", "status": ""}, {"name": "03-06-02", "status": ""}, {"name": "03-06-03", "status": null}, {"name": "03-06-04", "status": null}, {"name": "03-06-05", "status": null}, {"name": "03-06-06", "status": null}, {"name": "03-07-01", "status": ""}, {"name": "03-07-02", "status": ""}, {"name": "03-07-03", "status": null}, {"name": "03-07-04", "status": null}, {"name": "03-07-05", "status": null}, {"name": "03-07-06", "status": null}, {"name": "03-08-01", "status": "\u51bb\u7ed3"}, {"name": "03-08-02", "status": ""}, {"name": "03-08-03", "status": null}, {"name": "03-08-04", "status": null}, {"name": "03-08-05", "status": null}, {"name": "03-08-06", "status": null}, {"name": "03-09-01", "status": null}, {"name": "03-09-02", "status": ""}, {"name": "03-09-03", "status": null}, {"name": "03-09-04", "status": null}, {"name": "03-09-05", "status": null}, {"name": "03-09-06", "status": null}, {"name": "03-10-01", "status": null}, {"name": "03-10-02", "status": ""}, {"name": "03-10-03", "status": null}, {"name": "03-10-04", "status": null}, {"name": "03-10-05", "status": null}, {"name": "03-10-06", "status": null}, {"name": "03-11-01", "status": null}, {"name": "03-11-02", "status": ""}, {"name": "03-11-03", "status": null}, {"name": "03-11-04", "status": null}, {"name": "03-11-05", "status": null}, {"name": "03-11-06", "status": null}, {"name": "03-12-01", "status": ""}, {"name": "03-12-02", "status": ""}, {"name": "03-12-03", "status": null}, {"name": "03-12-04", "status": null}, {"name": "03-12-05", "status": null}, {"name": "03-12-06", "status": null}, {"name": "03-13-01", "status": ""}, {"name": "03-13-02", "status": ""}, {"name": "03-13-03", "status": null}, {"name": "03-13-04", "status": null}, {"name": "03-13-05", "status": null}, {"name": "03-13-06", "status": null}, {"name": "03-14-01", "status": null}, {"name": "03-14-02", "status": ""}, {"name": "03-14-03", "status": null}, {"name": "03-14-04", "status": null}, {"name": "03-14-05", "status": null}, {"name": "03-14-06", "status": null}, {"name": "03-15-01", "status": ""}, {"name": "03-15-02", "status": ""}, {"name": "03-15-03", "status": null}, {"name": "03-15-04", "status": null}, {"name": "03-15-05", "status": null}, {"name": "03-15-06", "status": null}, {"name": "03-16-01", "status": ""}, {"name": "03-16-02", "status": ""}, {"name": "03-16-03", "status": null}, {"name": "03-16-04", "status": null}, {"name": "03-16-05", "status": null}, {"name": "03-16-06", "status": null}, {"name": "03-17-01", "status": ""}, {"name": "03-17-02", "status": ""}, {"name": "03-17-03", "status": null}, {"name": "03-17-04", "status": null}, {"name": "03-17-05", "status": null}, {"name": "03-17-06", "status": null}, {"name": "03-18-01", "status": ""}, {"name": "03-18-02", "status": ""}, {"name": "03-18-03", "status": null}, {"name": "03-18-04", "status": null}, {"name": "03-18-05", "status": null}, {"name": "03-18-06", "status": null}, {"name": "03-19-01", "status": ""}, {"name": "03-19-02", "status": ""}, {"name": "03-19-03", "status": null}, {"name": "03-19-04", "status": null}, {"name": "03-19-05", "status": null}, {"name": "03-19-06", "status": null}, {"name": "03-20-01", "status": ""}, {"name": "03-20-02", "status": ""}, {"name": "03-20-03", "status": null}, {"name": "03-20-04", "status": null}, {"name": "03-20-05", "status": null}, {"name": "03-20-06", "status": null}, {"name": "03-21-01", "status": null}, {"name": "03-21-02", "status": null}, {"name": "03-21-03", "status": null}, {"name": "03-21-04", "status": null}, {"name": "03-21-05", "status": null}, {"name": "03-21-06", "status": null}, {"name": "03-22-01", "status": ""}, {"name": "03-22-02", "status": ""}, {"name": "03-22-03", "status": null}, {"name": "03-22-04", "status": null}, {"name": "03-22-05", "status": null}, {"name": "03-22-06", "status": null}, {"name": "03-23-01", "status": null}, {"name": "03-23-02", "status": null}, {"name": "03-23-03", "status": null}, {"name": "03-23-04", "status": null}, {"name": "03-23-05", "status": null}, {"name": "03-23-06", "status": null}, {"name": "03-24-01", "status": ""}, {"name": "03-24-02", "status": ""}, {"name": "03-24-03", "status": null}, {"name": "03-24-04", "status": null}, {"name": "03-24-05", "status": null}, {"name": "03-24-06", "status": null}, {"name": "03-25-01", "status": ""}, {"name": "03-25-02", "status": ""}, {"name": "03-25-03", "status": null}, {"name": "03-25-04", "status": null}, {"name": "03-25-05", "status": null}, {"name": "03-25-06", "status": null}, {"name": "03-26-01", "status": ""}, {"name": "03-26-02", "status": ""}, {"name": "03-26-03", "status": null}, {"name": "03-26-04", "status": null}, {"name": "03-26-05", "status": null}, {"name": "03-26-06", "status": null}, {"name": "03-27-01", "status": null}, {"name": "03-27-02", "status": null}, {"name": "03-27-03", "status": null}, {"name": "03-27-04", "status": null}, {"name": "03-27-05", "status": null}, {"name": "03-27-06", "status": null}, {"name": "03-28-01", "status": null}, {"name": "03-28-02", "status": ""}, {"name": "03-28-03", "status": null}, {"name": "03-28-04", "status": null}, {"name": "03-28-05", "status": null}, {"name": "03-28-06", "status": null}, {"name": "03-29-01", "status": ""}, {"name": "03-29-02", "status": ""}, {"name": "03-29-03", "status": null}, {"name": "03-29-04", "status": null}, {"name": "03-29-05", "status": null}, {"name": "03-29-06", "status": null}, {"name": "03-30-01", "status": ""}, {"name": "03-30-02", "status": ""}, {"name": "03-30-03", "status": null}, {"name": "03-30-04", "status": null}, {"name": "03-30-05", "status": null}, {"name": "03-30-06", "status": null}, {"name": "03-31-01", "status": ""}, {"name": "03-31-02", "status": ""}, {"name": "03-31-03", "status": null}, {"name": "03-31-04", "status": null}, {"name": "03-31-05", "status": null}, {"name": "03-31-06", "status": null}, {"name": "03-32-01", "status": ""}, {"name": "03-32-02", "status": ""}, {"name": "03-32-03", "status": null}, {"name": "03-32-04", "status": null}, {"name": "03-32-05", "status": null}, {"name": "03-32-06", "status": null}]}, {"name": "\u56db\u53f7\u8d27\u67b6", "list": [{"name": "04-02-01", "status": ""}, {"name": "04-02-02", "status": null}, {"name": "04-02-03", "status": null}, {"name": "04-02-04", "status": null}, {"name": "04-02-05", "status": null}, {"name": "04-02-06", "status": null}, {"name": "04-03-01", "status": ""}, {"name": "04-03-02", "status": null}, {"name": "04-03-03", "status": null}, {"name": "04-03-04", "status": null}, {"name": "04-03-05", "status": null}, {"name": "04-03-06", "status": null}, {"name": "04-04-01", "status": ""}, {"name": "04-04-02", "status": null}, {"name": "04-04-03", "status": null}, {"name": "04-04-04", "status": null}, {"name": "04-04-05", "status": null}, {"name": "04-04-06", "status": null}, {"name": "04-05-01", "status": ""}, {"name": "04-05-02", "status": null}, {"name": "04-05-03", "status": null}, {"name": "04-05-04", "status": null}, {"name": "04-05-05", "status": null}, {"name": "04-05-06", "status": null}, {"name": "04-06-01", "status": ""}, {"name": "04-06-02", "status": null}, {"name": "04-06-03", "status": null}, {"name": "04-06-04", "status": null}, {"name": "04-06-05", "status": null}, {"name": "04-06-06", "status": null}, {"name": "04-07-01", "status": ""}, {"name": "04-07-02", "status": null}, {"name": "04-07-03", "status": null}, {"name": "04-07-04", "status": null}, {"name": "04-07-05", "status": null}, {"name": "04-07-06", "status": null}, {"name": "04-08-01", "status": ""}, {"name": "04-08-02", "status": null}, {"name": "04-08-03", "status": null}, {"name": "04-08-04", "status": null}, {"name": "04-08-05", "status": null}, {"name": "04-08-06", "status": null}, {"name": "04-09-01", "status": ""}, {"name": "04-09-02", "status": null}, {"name": "04-09-03", "status": null}, {"name": "04-09-04", "status": null}, {"name": "04-09-05", "status": null}, {"name": "04-09-06", "status": null}, {"name": "04-10-01", "status": ""}, {"name": "04-10-02", "status": null}, {"name": "04-10-03", "status": null}, {"name": "04-10-04", "status": null}, {"name": "04-10-05", "status": null}, {"name": "04-10-06", "status": null}, {"name": "04-11-01", "status": null}, {"name": "04-11-02", "status": null}, {"name": "04-11-03", "status": null}, {"name": "04-11-04", "status": null}, {"name": "04-11-05", "status": null}, {"name": "04-11-06", "status": null}, {"name": "04-12-01", "status": null}, {"name": "04-12-02", "status": null}, {"name": "04-12-03", "status": null}, {"name": "04-12-04", "status": null}, {"name": "04-12-05", "status": null}, {"name": "04-12-06", "status": null}, {"name": "04-13-01", "status": ""}, {"name": "04-13-02", "status": null}, {"name": "04-13-03", "status": null}, {"name": "04-13-04", "status": null}, {"name": "04-13-05", "status": null}, {"name": "04-13-06", "status": null}, {"name": "04-14-01", "status": ""}, {"name": "04-14-02", "status": null}, {"name": "04-14-03", "status": null}, {"name": "04-14-04", "status": null}, {"name": "04-14-05", "status": null}, {"name": "04-14-06", "status": null}, {"name": "04-15-01", "status": ""}, {"name": "04-15-02", "status": null}, {"name": "04-15-03", "status": null}, {"name": "04-15-04", "status": null}, {"name": "04-15-05", "status": null}, {"name": "04-15-06", "status": null}, {"name": "04-16-01", "status": ""}, {"name": "04-16-02", "status": null}, {"name": "04-16-03", "status": null}, {"name": "04-16-04", "status": null}, {"name": "04-16-05", "status": null}, {"name": "04-16-06", "status": null}, {"name": "04-17-01", "status": ""}, {"name": "04-17-02", "status": null}, {"name": "04-17-03", "status": null}, {"name": "04-17-04", "status": null}, {"name": "04-17-05", "status": null}, {"name": "04-17-06", "status": null}, {"name": "04-18-01", "status": ""}, {"name": "04-18-02", "status": null}, {"name": "04-18-03", "status": null}, {"name": "04-18-04", "status": null}, {"name": "04-18-05", "status": null}, {"name": "04-18-06", "status": null}, {"name": "04-19-01", "status": ""}, {"name": "04-19-02", "status": null}, {"name": "04-19-03", "status": null}, {"name": "04-19-04", "status": null}, {"name": "04-19-05", "status": null}, {"name": "04-19-06", "status": null}, {"name": "04-20-01", "status": ""}, {"name": "04-20-02", "status": null}, {"name": "04-20-03", "status": null}, {"name": "04-20-04", "status": null}, {"name": "04-20-05", "status": null}, {"name": "04-20-06", "status": null}, {"name": "04-21-01", "status": ""}, {"name": "04-21-02", "status": null}, {"name": "04-21-03", "status": null}, {"name": "04-21-04", "status": null}, {"name": "04-21-05", "status": null}, {"name": "04-21-06", "status": null}, {"name": "04-22-01", "status": ""}, {"name": "04-22-02", "status": null}, {"name": "04-22-03", "status": ""}, {"name": "04-22-04", "status": null}, {"name": "04-22-05", "status": null}, {"name": "04-22-06", "status": null}, {"name": "04-23-01", "status": null}, {"name": "04-23-02", "status": ""}, {"name": "04-23-03", "status": ""}, {"name": "04-23-04", "status": null}, {"name": "04-23-05", "status": null}, {"name": "04-23-06", "status": null}, {"name": "04-24-01", "status": ""}, {"name": "04-24-02", "status": ""}, {"name": "04-24-03", "status": ""}, {"name": "04-24-04", "status": null}, {"name": "04-24-05", "status": null}, {"name": "04-24-06", "status": null}, {"name": "04-25-01", "status": ""}, {"name": "04-25-02", "status": ""}, {"name": "04-25-03", "status": null}, {"name": "04-25-04", "status": null}, {"name": "04-25-05", "status": null}, {"name": "04-25-06", "status": null}, {"name": "04-26-01", "status": ""}, {"name": "04-26-02", "status": null}, {"name": "04-26-03", "status": ""}, {"name": "04-26-04", "status": null}, {"name": "04-26-05", "status": null}, {"name": "04-26-06", "status": null}, {"name": "04-27-01", "status": ""}, {"name": "04-27-02", "status": null}, {"name": "04-27-03", "status": ""}, {"name": "04-27-04", "status": null}, {"name": "04-27-05", "status": null}, {"name": "04-27-06", "status": null}, {"name": "04-28-01", "status": ""}, {"name": "04-28-02", "status": null}, {"name": "04-28-03", "status": null}, {"name": "04-28-04", "status": null}, {"name": "04-28-05", "status": null}, {"name": "04-28-06", "status": null}, {"name": "04-29-01", "status": ""}, {"name": "04-29-02", "status": null}, {"name": "04-29-03", "status": null}, {"name": "04-29-04", "status": null}, {"name": "04-29-05", "status": null}, {"name": "04-29-06", "status": null}, {"name": "04-30-01", "status": ""}, {"name": "04-30-02", "status": null}, {"name": "04-30-03", "status": null}, {"name": "04-30-04", "status": null}, {"name": "04-30-05", "status": null}, {"name": "04-30-06", "status": null}, {"name": "04-31-01", "status": ""}, {"name": "04-31-02", "status": ""}, {"name": "04-31-03", "status": null}, {"name": "04-31-04", "status": null}, {"name": "04-31-05", "status": null}, {"name": "04-31-06", "status": null}, {"name": "04-32-01", "status": ""}, {"name": "04-32-02", "status": ""}, {"name": "04-32-03", "status": null}, {"name": "04-32-04", "status": null}, {"name": "04-32-05", "status": null}, {"name": "04-32-06", "status": null}]}, {"name": "\u4e94\u53f7\u8d27\u67b6", "list": [{"name": "05-01-03", "status": null}, {"name": "05-01-04", "status": null}, {"name": "05-01-05", "status": null}, {"name": "05-02-01", "status": "\u5f85\u68c0"}, {"name": "05-02-02", "status": "\u5f85\u68c0"}, {"name": "05-02-03", "status": null}, {"name": "05-02-04", "status": null}, {"name": "05-02-05", "status": null}, {"name": "05-02-06", "status": null}, {"name": "05-03-01", "status": "\u5f85\u68c0"}, {"name": "05-03-02", "status": "\u5f85\u68c0"}, {"name": "05-03-03", "status": null}, {"name": "05-03-04", "status": null}, {"name": "05-03-05", "status": null}, {"name": "05-03-06", "status": null}, {"name": "05-04-01", "status": "\u5f85\u68c0"}, {"name": "05-04-02", "status": "\u5f85\u68c0"}, {"name": "05-04-03", "status": null}, {"name": "05-04-04", "status": null}, {"name": "05-04-05", "status": null}, {"name": "05-04-06", "status": null}, {"name": "05-05-01", "status": "\u5f85\u68c0"}, {"name": "05-05-02", "status": "\u5f85\u68c0"}, {"name": "05-05-03", "status": null}, {"name": "05-05-04", "status": null}, {"name": "05-05-05", "status": null}, {"name": "05-05-06", "status": null}, {"name": "05-06-01", "status": "\u5f85\u68c0"}, {"name": "05-06-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-06-03", "status": null}, {"name": "05-06-04", "status": null}, {"name": "05-06-05", "status": null}, {"name": "05-06-06", "status": null}, {"name": "05-07-01", "status": "\u5f85\u68c0"}, {"name": "05-07-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-07-03", "status": null}, {"name": "05-07-04", "status": null}, {"name": "05-07-05", "status": null}, {"name": "05-07-06", "status": null}, {"name": "05-08-01", "status": "\u5f85\u68c0"}, {"name": "05-08-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-08-03", "status": null}, {"name": "05-08-04", "status": null}, {"name": "05-08-05", "status": null}, {"name": "05-08-06", "status": null}, {"name": "05-09-01", "status": "\u5f85\u68c0"}, {"name": "05-09-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-09-03", "status": null}, {"name": "05-09-04", "status": null}, {"name": "05-09-05", "status": null}, {"name": "05-09-06", "status": null}, {"name": "05-10-01", "status": "\u5f85\u68c0"}, {"name": "05-10-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-10-03", "status": null}, {"name": "05-10-04", "status": null}, {"name": "05-10-05", "status": null}, {"name": "05-10-06", "status": null}, {"name": "05-11-01", "status": "\u5f85\u68c0"}, {"name": "05-11-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-11-03", "status": null}, {"name": "05-11-04", "status": null}, {"name": "05-11-05", "status": null}, {"name": "05-11-06", "status": null}, {"name": "05-12-01", "status": "\u5f85\u68c0"}, {"name": "05-12-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-12-03", "status": null}, {"name": "05-12-04", "status": null}, {"name": "05-12-05", "status": null}, {"name": "05-12-06", "status": null}, {"name": "05-13-01", "status": "\u5f85\u68c0"}, {"name": "05-13-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-13-03", "status": null}, {"name": "05-13-04", "status": null}, {"name": "05-13-05", "status": null}, {"name": "05-13-06", "status": null}, {"name": "05-14-01", "status": "\u5f85\u68c0"}, {"name": "05-14-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-14-03", "status": null}, {"name": "05-14-04", "status": null}, {"name": "05-14-05", "status": null}, {"name": "05-14-06", "status": null}, {"name": "05-15-01", "status": "\u5f85\u68c0"}, {"name": "05-15-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-15-03", "status": null}, {"name": "05-15-04", "status": null}, {"name": "05-15-05", "status": null}, {"name": "05-15-06", "status": null}, {"name": "05-16-01", "status": "\u5f85\u68c0"}, {"name": "05-16-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-16-03", "status": null}, {"name": "05-16-04", "status": null}, {"name": "05-16-05", "status": null}, {"name": "05-16-06", "status": null}, {"name": "05-17-01", "status": "\u5f85\u68c0"}, {"name": "05-17-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-17-03", "status": null}, {"name": "05-17-04", "status": null}, {"name": "05-17-05", "status": null}, {"name": "05-17-06", "status": null}, {"name": "05-18-01", "status": "\u5f85\u68c0"}, {"name": "05-18-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-18-03", "status": null}, {"name": "05-18-04", "status": null}, {"name": "05-18-05", "status": null}, {"name": "05-18-06", "status": null}, {"name": "05-19-01", "status": "\u5f85\u68c0"}, {"name": "05-19-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-19-03", "status": null}, {"name": "05-19-04", "status": null}, {"name": "05-19-05", "status": null}, {"name": "05-19-06", "status": null}, {"name": "05-20-01", "status": "\u5f85\u68c0"}, {"name": "05-20-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-20-03", "status": null}, {"name": "05-20-04", "status": null}, {"name": "05-20-05", "status": null}, {"name": "05-20-06", "status": null}, {"name": "05-21-01", "status": "\u5f85\u68c0"}, {"name": "05-21-02", "status": "\u5f85\u5904\u7406"}, {"name": "05-21-03", "status": null}, {"name": "05-21-04", "status": null}, {"name": "05-21-05", "status": null}, {"name": "05-21-06", "status": null}, {"name": "05-22-01", "status": null}, {"name": "05-22-02", "status": null}, {"name": "05-22-03", "status": "\u5f85\u68c0"}, {"name": "05-22-04", "status": null}, {"name": "05-22-05", "status": null}, {"name": "05-22-06", "status": null}, {"name": "05-23-01", "status": null}, {"name": "05-23-02", "status": null}, {"name": "05-23-03", "status": "\u5f85\u68c0"}, {"name": "05-23-04", "status": null}, {"name": "05-23-05", "status": null}, {"name": "05-23-06", "status": null}, {"name": "05-24-01", "status": null}, {"name": "05-24-02", "status": null}, {"name": "05-24-03", "status": "\u5f85\u68c0"}, {"name": "05-24-04", "status": null}, {"name": "05-24-05", "status": null}, {"name": "05-24-06", "status": null}, {"name": "05-25-01", "status": null}, {"name": "05-25-02", "status": "\u5f85\u68c0"}, {"name": "05-25-03", "status": "\u5f85\u68c0"}, {"name": "05-25-04", "status": null}, {"name": "05-25-05", "status": null}, {"name": "05-25-06", "status": null}, {"name": "05-26-01", "status": null}, {"name": "05-26-02", "status": "\u5f85\u68c0"}, {"name": "05-26-03", "status": "\u5f85\u68c0"}, {"name": "05-26-04", "status": null}, {"name": "05-26-05", "status": null}, {"name": "05-26-06", "status": null}, {"name": "05-27-01", "status": null}, {"name": "05-27-02", "status": "\u5f85\u68c0"}, {"name": "05-27-03", "status": "\u5f85\u68c0"}, {"name": "05-27-04", "status": null}, {"name": "05-27-05", "status": null}, {"name": "05-27-06", "status": null}, {"name": "05-28-01", "status": null}, {"name": "05-28-02", "status": "\u5f85\u68c0"}, {"name": "05-28-03", "status": "\u5f85\u68c0"}, {"name": "05-28-04", "status": null}, {"name": "05-28-05", "status": null}, {"name": "05-28-06", "status": null}, {"name": "05-29-01", "status": null}, {"name": "05-29-02", "status": "\u5f85\u68c0"}, {"name": "05-29-03", "status": "\u5f85\u68c0"}, {"name": "05-29-04", "status": null}, {"name": "05-29-05", "status": null}, {"name": "05-29-06", "status": null}, {"name": "05-30-01", "status": null}, {"name": "05-30-02", "status": "\u5f85\u68c0"}, {"name": "05-30-03", "status": "\u5f85\u68c0"}, {"name": "05-30-04", "status": null}, {"name": "05-30-05", "status": null}, {"name": "05-30-06", "status": null}, {"name": "05-31-01", "status": "\u5f85\u5904\u7406"}, {"name": "05-31-02", "status": "\u5f85\u68c0"}, {"name": "05-31-03", "status": "\u5f85\u68c0"}, {"name": "05-31-04", "status": null}, {"name": "05-31-05", "status": null}, {"name": "05-31-06", "status": null}, {"name": "05-32-01", "status": null}, {"name": "05-32-02", "status": "\u5f85\u68c0"}, {"name": "05-32-03", "status": "\u5f85\u5904\u7406"}, {"name": "05-32-04", "status": null}, {"name": "05-32-05", "status": null}, {"name": "05-32-06", "status": null}, {"name": "05-33-01", "status": null}, {"name": "05-33-02", "status": "\u5f85\u68c0"}, {"name": "05-33-03", "status": "\u5f85\u5904\u7406"}, {"name": "05-33-04", "status": null}, {"name": "05-33-05", "status": null}, {"name": "05-33-06", "status": null}, {"name": "05-34-01", "status": null}, {"name": "05-34-02", "status": "\u5f85\u68c0"}, {"name": "05-34-03", "status": "\u5f85\u5904\u7406"}, {"name": "05-34-04", "status": ""}, {"name": "05-34-05", "status": null}, {"name": "05-34-06", "status": null}]}, {"name": "\u516d\u53f7\u8d27\u67b6", "list": [{"name": "06-02-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-02-02", "status": "\u5f85\u68c0"}, {"name": "06-02-03", "status": "\u5f85\u68c0"}, {"name": "06-02-04", "status": "\u5f85\u5904\u7406"}, {"name": "06-02-05", "status": "\u5f85\u68c0"}, {"name": "06-02-06", "status": null}, {"name": "06-03-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-03-02", "status": "\u5f85\u68c0"}, {"name": "06-03-03", "status": "\u5f85\u68c0"}, {"name": "06-03-04", "status": "\u5f85\u5904\u7406"}, {"name": "06-03-05", "status": "\u5f85\u68c0"}, {"name": "06-03-06", "status": null}, {"name": "06-04-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-04-02", "status": "\u5f85\u68c0"}, {"name": "06-04-03", "status": "\u5f85\u68c0"}, {"name": "06-04-04", "status": "\u5f85\u5904\u7406"}, {"name": "06-04-05", "status": "\u5f85\u68c0"}, {"name": "06-04-06", "status": null}, {"name": "06-05-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-05-02", "status": "\u5f85\u68c0"}, {"name": "06-05-03", "status": "\u5f85\u68c0"}, {"name": "06-05-04", "status": "\u5f85\u5904\u7406"}, {"name": "06-05-05", "status": "\u5f85\u68c0"}, {"name": "06-05-06", "status": null}, {"name": "06-06-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-06-02", "status": "\u5f85\u68c0"}, {"name": "06-06-03", "status": "\u5f85\u68c0"}, {"name": "06-06-04", "status": null}, {"name": "06-06-05", "status": "\u5f85\u68c0"}, {"name": "06-06-06", "status": null}, {"name": "06-07-01", "status": null}, {"name": "06-07-02", "status": "\u5f85\u68c0"}, {"name": "06-07-03", "status": "\u5f85\u68c0"}, {"name": "06-07-04", "status": null}, {"name": "06-07-05", "status": "\u5f85\u68c0"}, {"name": "06-07-06", "status": null}, {"name": "06-08-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-08-02", "status": "\u5f85\u68c0"}, {"name": "06-08-03", "status": "\u5f85\u68c0"}, {"name": "06-08-04", "status": null}, {"name": "06-08-05", "status": "\u5f85\u68c0"}, {"name": "06-08-06", "status": null}, {"name": "06-09-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-09-02", "status": "\u5f85\u68c0"}, {"name": "06-09-03", "status": "\u5f85\u68c0"}, {"name": "06-09-04", "status": null}, {"name": "06-09-05", "status": "\u5f85\u68c0"}, {"name": "06-09-06", "status": null}, {"name": "06-10-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-10-02", "status": "\u5f85\u68c0"}, {"name": "06-10-03", "status": "\u5f85\u68c0"}, {"name": "06-10-04", "status": null}, {"name": "06-10-05", "status": "\u5f85\u68c0"}, {"name": "06-10-06", "status": null}, {"name": "06-11-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-11-02", "status": "\u5f85\u68c0"}, {"name": "06-11-03", "status": "\u5f85\u68c0"}, {"name": "06-11-04", "status": null}, {"name": "06-11-05", "status": "\u5f85\u68c0"}, {"name": "06-11-06", "status": null}, {"name": "06-12-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-12-02", "status": "\u5f85\u68c0"}, {"name": "06-12-03", "status": "\u5f85\u68c0"}, {"name": "06-12-04", "status": null}, {"name": "06-12-05", "status": "\u5f85\u68c0"}, {"name": "06-12-06", "status": null}, {"name": "06-13-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-13-02", "status": "\u5f85\u68c0"}, {"name": "06-13-03", "status": "\u5f85\u68c0"}, {"name": "06-13-04", "status": null}, {"name": "06-13-05", "status": "\u5f85\u68c0"}, {"name": "06-13-06", "status": null}, {"name": "06-14-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-14-02", "status": "\u5f85\u68c0"}, {"name": "06-14-03", "status": "\u5f85\u68c0"}, {"name": "06-14-04", "status": null}, {"name": "06-14-05", "status": "\u5f85\u68c0"}, {"name": "06-14-06", "status": null}, {"name": "06-15-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-15-02", "status": "\u5f85\u68c0"}, {"name": "06-15-03", "status": "\u5f85\u68c0"}, {"name": "06-15-04", "status": null}, {"name": "06-15-05", "status": "\u5f85\u68c0"}, {"name": "06-15-06", "status": null}, {"name": "06-16-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-16-02", "status": "\u5f85\u68c0"}, {"name": "06-16-03", "status": "\u5f85\u68c0"}, {"name": "06-16-04", "status": null}, {"name": "06-16-05", "status": "\u5f85\u68c0"}, {"name": "06-16-06", "status": null}, {"name": "06-17-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-17-02", "status": "\u5f85\u68c0"}, {"name": "06-17-03", "status": "\u5f85\u68c0"}, {"name": "06-17-04", "status": null}, {"name": "06-17-05", "status": "\u5f85\u68c0"}, {"name": "06-17-06", "status": null}, {"name": "06-18-01", "status": null}, {"name": "06-18-02", "status": "\u5f85\u68c0"}, {"name": "06-18-03", "status": "\u5f85\u68c0"}, {"name": "06-18-04", "status": null}, {"name": "06-18-05", "status": "\u5f85\u68c0"}, {"name": "06-18-06", "status": null}, {"name": "06-19-01", "status": null}, {"name": "06-19-02", "status": "\u5f85\u68c0"}, {"name": "06-19-03", "status": "\u5f85\u68c0"}, {"name": "06-19-04", "status": null}, {"name": "06-19-05", "status": "\u5f85\u68c0"}, {"name": "06-19-06", "status": null}, {"name": "06-20-01", "status": null}, {"name": "06-20-02", "status": "\u5f85\u68c0"}, {"name": "06-20-03", "status": "\u5f85\u68c0"}, {"name": "06-20-04", "status": null}, {"name": "06-20-05", "status": "\u5f85\u68c0"}, {"name": "06-20-06", "status": null}, {"name": "06-21-01", "status": null}, {"name": "06-21-02", "status": "\u5f85\u68c0"}, {"name": "06-21-03", "status": "\u5f85\u68c0"}, {"name": "06-21-04", "status": ""}, {"name": "06-21-05", "status": "\u5f85\u68c0"}, {"name": "06-21-06", "status": null}, {"name": "06-22-01", "status": "\u5f85\u68c0"}, {"name": "06-22-02", "status": "\u5f85\u68c0"}, {"name": "06-22-03", "status": null}, {"name": "06-22-04", "status": "\u5f85\u68c0"}, {"name": "06-22-05", "status": "\u5f85\u68c0"}, {"name": "06-22-06", "status": ""}, {"name": "06-23-01", "status": "\u5f85\u68c0"}, {"name": "06-23-02", "status": "\u5f85\u68c0"}, {"name": "06-23-03", "status": null}, {"name": "06-23-04", "status": "\u5f85\u68c0"}, {"name": "06-23-05", "status": "\u5f85\u68c0"}, {"name": "06-23-06", "status": null}, {"name": "06-24-01", "status": "\u5f85\u68c0"}, {"name": "06-24-02", "status": "\u5f85\u68c0"}, {"name": "06-24-03", "status": null}, {"name": "06-24-04", "status": "\u5f85\u68c0"}, {"name": "06-24-05", "status": "\u5f85\u68c0"}, {"name": "06-24-06", "status": null}, {"name": "06-25-01", "status": "\u5f85\u68c0"}, {"name": "06-25-02", "status": "\u5f85\u68c0"}, {"name": "06-25-03", "status": null}, {"name": "06-25-04", "status": "\u5f85\u68c0"}, {"name": "06-25-05", "status": "\u5f85\u68c0"}, {"name": "06-25-06", "status": null}, {"name": "06-26-01", "status": "\u5f85\u68c0"}, {"name": "06-26-02", "status": "\u5f85\u68c0"}, {"name": "06-26-03", "status": null}, {"name": "06-26-04", "status": "\u5f85\u68c0"}, {"name": "06-26-05", "status": "\u5f85\u68c0"}, {"name": "06-26-06", "status": null}, {"name": "06-27-01", "status": "\u5f85\u68c0"}, {"name": "06-27-02", "status": "\u5f85\u68c0"}, {"name": "06-27-03", "status": null}, {"name": "06-27-04", "status": "\u5f85\u68c0"}, {"name": "06-27-05", "status": "\u5f85\u68c0"}, {"name": "06-27-06", "status": null}, {"name": "06-28-01", "status": "\u5f85\u68c0"}, {"name": "06-28-02", "status": "\u5f85\u68c0"}, {"name": "06-28-03", "status": null}, {"name": "06-28-04", "status": "\u5f85\u68c0"}, {"name": "06-28-05", "status": "\u5f85\u68c0"}, {"name": "06-28-06", "status": null}, {"name": "06-29-01", "status": null}, {"name": "06-29-02", "status": "\u5f85\u68c0"}, {"name": "06-29-03", "status": null}, {"name": "06-29-04", "status": "\u5f85\u68c0"}, {"name": "06-29-05", "status": "\u5f85\u68c0"}, {"name": "06-29-06", "status": null}, {"name": "06-30-01", "status": null}, {"name": "06-30-02", "status": "\u5f85\u68c0"}, {"name": "06-30-03", "status": null}, {"name": "06-30-04", "status": "\u5f85\u68c0"}, {"name": "06-30-05", "status": "\u5f85\u68c0"}, {"name": "06-30-06", "status": null}, {"name": "06-31-01", "status": "\u5f85\u5904\u7406"}, {"name": "06-31-02", "status": "\u5f85\u68c0"}, {"name": "06-31-03", "status": null}, {"name": "06-31-04", "status": "\u5f85\u68c0"}, {"name": "06-31-05", "status": null}, {"name": "06-31-06", "status": null}, {"name": "06-32-01", "status": null}, {"name": "06-32-02", "status": "\u5f85\u68c0"}, {"name": "06-32-03", "status": null}, {"name": "06-32-04", "status": "\u5f85\u68c0"}, {"name": "06-32-05", "status": null}, {"name": "06-32-06", "status": null}, {"name": "06-33-01", "status": "\u5f85\u68c0"}, {"name": "06-33-02", "status": "\u5f85\u68c0"}, {"name": "06-33-03", "status": null}, {"name": "06-33-04", "status": "\u5f85\u68c0"}, {"name": "06-33-05", "status": null}, {"name": "06-33-06", "status": null}, {"name": "06-34-01", "status": "\u5f85\u68c0"}, {"name": "06-34-02", "status": "\u5f85\u68c0"}, {"name": "06-34-03", "status": ""}, {"name": "06-34-04", "status": "\u5f85\u68c0"}, {"name": "06-34-05", "status": null}, {"name": "06-34-06", "status": null}]}];
        if (data && data.length > 0) {
          if (this.type === '1') {
            data.forEach((item, index) => {
              let list = item.list;
              list.sort(this.sortBy('name'));
            })
          }
          this.storagebinList = data
        }*/
      },
      redirect(binum, status) {
        if (status == '') {
          status = 'empty'
        }
        this.$router.push(`/detail/${this.type}/${binum}/${status}/warehouse`)
      },
      btnClass(status) {
        let btnClazz = 'white-btn'
        if (status === '待检') {
          btnClazz = 'red-btn'
        } else if (status === '冻结') {
          btnClazz = 'yellow-btn'
        } else if (status === '') {
          btnClazz = 'green-btn'
        } else if (status === '待处理') {
          btnClazz = 'orange-btn'
        }
        return btnClazz
      },
      sortBy (field) {
        return function(a, b) {
          let value1 = a[field].substring(6, 8);
          let value2 = b[field].substring(6, 8);
          return value2 - value1;
        }
      },
      isShowBr(item, subIndex) {
        let list = item.list
        let currName = list[subIndex].name.substring(0, 2) + list[subIndex].name.substring(6, 8);
        let lastName = list[subIndex > 0 ? subIndex - 1 : 0 ].name.substring(0, 2)
          + list[subIndex > 0 ? subIndex - 1 : 0 ].name.substring(6, 8);
        if (currName !== lastName) {
          return true
        }
        return false
      },
      isShowNullDiv(item, subIndex) {
        let list = item.list

        let curr = list[subIndex].name
        let currName = curr.substring(3, 5);

        let last = list[subIndex > 0 ? subIndex - 1 : 0 ].name
        let lastName = last.substring(3, 5);

        let flag = false
        if (currName === '02' && lastName !== '01') {
          flag = true
        }
        return flag
      }
    },
    components: {
      GoBack: GoBack
    },
    created() {
      this.init()
    }
  }
</script>

<style lang="less" scoped>
  .tl {
    text-align: left;
  }
  .special-content-div {
    width: 4000px;
    padding: 30px;
    .storage-col {
      margin-bottom: 30px;
      .storage-left-col {
        width: 130px;
        text-align: right;
        margin-right: 20px;
        font-size: 18px;
        font-weight: 600;
        color: #333333;
      }
      .storage-right-col {
        width: calc(~"100% - 150px");
        .storage-item-btn {
          margin: 0 5px 5px 0;
        }
        .div-null {
          width: 100px;
          margin: 2px;
          display: inline-block;
        }
      }
    }
  }
  .top-div {
    display: flex;
    padding: 30px;
  }
  .content-div {
    /*margin-top: 50px;*/
    /*width: 4000px;*/
    padding: 30px;
    .storagebin-btn {
      width: 100%;
      height: 90px;
      font-size: 30px;
      font-weight: 600;
    }
  }
  .item-row {
    line-height: 40px;
    font-size: 18px;
    padding: 2px 0 2px 0;
    color: #000000;
    div{
      border-radius: 4px;
    }
  }
  .subItem-left-col {
    text-align: right;
    background-color: #d3dce6;
    padding-right: 10px;
  }
  .subItem-right-col {
    padding: 0 5px 0 5px;
    div {
      padding-left: 10px;
    }
  }
  .top-div {
    .el-col-3 {
      width: 13.8%;
      .item-row {
        font-weight: 500;
      }
    }
    .el-col-6 {
      width: 17%;
      padding-left: 50px;
      .item-row {
        font-weight: 800;
      }
    }
    .el-col-9 {
      width: 40%;
    }
    .el-col-15 {
      width: 60%;
    }
  }
  .green {
    background-color: #19ce50;
  }
  .yellow {
    background-color: #ffff33;
  }
  .red {
    background-color: #f5222d;
  }
</style>
