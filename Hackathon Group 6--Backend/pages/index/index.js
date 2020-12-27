//index.js
//获取应用实例
const app = getApp()
var bindblur;

Page({
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },

  bindblur:function(e){
    // console.log('1111111:', e.detail.value);
    bindblur = e.detail.value;
  },

  onLoad: function () {
    // wx.login({
    //   success (res) {
    //     if (res.code) {
    //       data.openid = res.code
    //     } else {
    //       console.log('登录失败！' + res.errMsg)
    //     }
    //   }
    // })

    var that = this;
    wx.request({
      url: 'http://39.108.229.166:5000/get_basic_info',
      method:'POST',
      data:{
        'file_name':'bixi_sound.m4a'
      },
      success:function(res){
        console.log(res.data.comments.reverse())
        that.setData({
          pl_list: res.data.comments.reverse()
        })
      }
    });

    this.audioCtx = wx.createAudioContext('myAudio')
    wx.request({
      url: 'http://39.108.229.166:5000/',
      success:function(result){
          console.log(result.data)
      }
    })
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true,
        })
      }
    } else {
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true,
          })
        }
      })
    }
  },
  data: {
    // poster: 'http://127.0.0.1:5001/static/files/bixi/bixi_sound.m4a',
    name: '上学的一天',
    author: '碧溪小学的一位二年级同学',
    src: 'http://39.108.229.166:5000/static/files/bixi/bixi_sound.m4a',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    openid:'',
    pl_list: [],
    state: ""
  },
  cmtUpload: function () {
    console.log('111')
    wx.request({
      url: 'http://39.108.229.166:5000/set_comment',
      method:'POST',
      data:{
        'userinfo':this.data.userInfo,
        'body':bindblur,
        'file_name':'bixi_sound.m4a'
      }
    });
    this.setData({
      state: "发表成功，请刷新后查看。"
    });
  },
  commentTest: function () {
  }
})
