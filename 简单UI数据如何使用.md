# 简单UI数据如何使用

`TVSUserInterface.Show`指令承载了UI数据。终端可以从这里取得用来展示的UI数据。



```json
{
	"header": {
		"dialogRequestId": "dialogRequestIddialogRequestId",
		"messageId": "TvsUserInterface-Show-MessageId-20200207T142444-1379663193",
		"name": "Show",
		"namespace": "TvsUserInterface"
	},
	"payload": {
		"baseInfo": {
			"sessionComplete": true
		},
		"errMsg": "STATUS_DEFAULT_REPLY",
		"jsonUI": {
			"compress": "none",
			"data": "{ \"baseInfo\": { \"skillIcon\": \"\", \"skillName\": \"\" }, \"controlInfo\": { \"audioConsole\": \"true\", \"orientation\": \"portrait\", \"textSpeak\": \"true\", \"type\": \"TEXT\", \"version\": \"1.0.0\" }, \"globalInfo\": { \"backgroundAudio\": { \"metadata\": { \"offsetInMilliseconds\": 0, \"totalMilliseconds\": 0 }, \"stream\": { \"url\": \"\" } }, \"backgroundImage\": { \"contentDescription\": \"\", \"sources\": [  ] }, \"seeMore\": \"\" }, \"listItems\": [ { \"audio\": { \"metadata\": { \"offsetInMilliseconds\": 0, \"totalMilliseconds\": 0 }, \"stream\": { \"url\": \"\" } }, \"htmlView\": \"\", \"image\": { \"contentDescription\": \"\", \"sources\": [  ] }, \"mediaId\": \"\", \"textContent\": \"你好啊，我很喜欢你\", \"title\": \"\", \"video\": { \"metadata\": { \"offsetInMilliseconds\": 0, \"totalMilliseconds\": 0 }, \"sources\": [  ] } } ], \"templateInfo\": { \"t_id\": \"\" } }",
			"query": "你好",
			"tipsText": ""
		},
		"retCode": 0,
		"session": "",
		"token": "Custom:0:chat:chat:chat:chat::0:0:0@TvsUserInterface-Show-Token-20200207T142444-0493548106"
	}
}
```



其`payload.jsonUI`内承载了UI数据


| 参数名           | 类型       | 描述                  |
| ------------- | -------- | ------------------- |
| `compress` | string      | `data`字段压缩算法 ，目前为`none`  |
| `data` | string        | UI 模板数据json的字符串结构，其定义遵循[这个文档](https://github.com/TencentDingdang/tvs-tools/blob/master/Tsk%20Protocol/%E6%8A%80%E8%83%BD%E6%95%B0%E6%8D%AE%E8%A7%84%E8%8C%83_V3.md) |
| `query` | string        | 用户请求query                 |
| `tipsText` | string        | 展示语                 |



最简单的应用，只关心展示给用户的文本。可以按照下面方法取得展示文本。

 展示文本需要`tipsText`与`UI模板数据`（data字段）的部分内容拼接。

处理`UI模板数据`（data字段），假如`controlInfo.type`为`TEXT`，按顺序拼接`listItems.title`、`listItems.subTitle`、`listItems.textContent`的字段内容。`listItems`是数组，假如`listItems`有多个子元素。那么依次遍历每个子元素进行拼接。文本拼接使用的分割符可以自行定义。简单的描述如下：

```
showText = tipsText
for item in listItems
   showText += item.title
   showText += 分隔符
   showText += item.subTitle
   showText += 分隔符
   showText += item.textContext
   showText += 分隔符
```



*示例*

UI数据示例如下：

```json
"jsonUI": {
	"compress": "none",
	"data": "{ \"baseInfo\": { \"skillIcon\": \"\", \"skillName\": \"\" }, \"controlInfo\": { \"audioConsole\": \"true\", \"orientation\": \"portrait\", \"textSpeak\": \"true\", \"type\": \"TEXT\", \"version\": \"1.0.0\" }, \"globalInfo\": { \"backgroundAudio\": { \"metadata\": { \"offsetInMilliseconds\": 0, \"totalMilliseconds\": 0 }, \"stream\": { \"url\": \"\" } }, \"backgroundImage\": { \"contentDescription\": \"\", \"sources\": [  ] }, \"seeMore\": \"\" }, \"listItems\": [ { \"audio\": { \"metadata\": { \"offsetInMilliseconds\": 0, \"totalMilliseconds\": 0 }, \"stream\": { \"url\": \"\" } }, \"htmlView\": \"\", \"image\": { \"contentDescription\": \"\", \"sources\": [  ] }, \"mediaId\": \"\", \"textContent\": \"你好啊，我很喜欢你\", \"title\": \"\", \"video\": { \"metadata\": { \"offsetInMilliseconds\": 0, \"totalMilliseconds\": 0 }, \"sources\": [  ] } } ], \"templateInfo\": { \"t_id\": \"\" } }",
	"query": "你好",
	"tipsText": "我是tipsText"
}
```

示例数据，拼接结果为`我是tipsText。你好啊，我很喜欢你`





