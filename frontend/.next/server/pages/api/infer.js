"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/api/infer";
exports.ids = ["pages/api/infer"];
exports.modules = {

/***/ "(api)/./src/pages/api/infer.ts":
/*!********************************!*\
  !*** ./src/pages/api/infer.ts ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ handler)\n/* harmony export */ });\n// تابع ارزیابی عبارات منطقی\nfunction evaluateLogicalExpression(expression) {\n    // حذف فاصله‌های اضافی\n    const cleanExpression = expression.trim().toUpperCase();\n    // بررسی عملگرها\n    if (cleanExpression.includes(\"AND\")) {\n        const parts = cleanExpression.split(\"AND\").map((part)=>part.trim());\n        return `AND operation with operands: ${parts.join(\" and \")}`;\n    } else if (cleanExpression.includes(\"OR\")) {\n        const parts1 = cleanExpression.split(\"OR\").map((part)=>part.trim());\n        return `OR operation with operands: ${parts1.join(\" or \")}`;\n    } else if (cleanExpression.includes(\"NOT\")) {\n        const operand = cleanExpression.replace(\"NOT\", \"\").trim();\n        return `NOT operation on: ${operand}`;\n    }\n    return \"Invalid expression - please use AND, OR, or NOT operators\";\n}\nfunction handler(req, res) {\n    try {\n        if (req.method !== \"POST\") {\n            console.log(\"Invalid method:\", req.method);\n            return res.status(405).json({\n                result: \"Method not allowed\",\n                success: false\n            });\n        }\n        const { expression  } = req.body;\n        console.log(\"Received expression:\", expression);\n        if (!expression || typeof expression !== \"string\") {\n            return res.status(400).json({\n                result: \"Invalid input expression\",\n                success: false\n            });\n        }\n        // ارزیابی عبارت منطقی\n        const result = evaluateLogicalExpression(expression);\n        console.log(\"Evaluation result:\", result);\n        return res.status(200).json({\n            result,\n            success: true\n        });\n    } catch (error) {\n        console.error(\"API Error:\", error);\n        return res.status(500).json({\n            result: \"Server error\",\n            success: false\n        });\n    }\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,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UUFDbkMsT0FBT1QsR0FBRyxDQUFDSSxNQUFNLENBQUMsR0FBRyxDQUFDLENBQUNDLElBQUksQ0FBQztZQUMxQkMsTUFBTSxFQUFFLGNBQWM7WUFDdEJDLE9BQU8sRUFBRSxLQUFLO1NBQ2YsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztBQUNILENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3NyYy9wYWdlcy9hcGkvaW5mZXIudHM/MTA4YyJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgdHlwZSB7IE5leHRBcGlSZXF1ZXN0LCBOZXh0QXBpUmVzcG9uc2UgfSBmcm9tICduZXh0JztcclxuXHJcbnR5cGUgRGF0YSA9IHtcclxuICByZXN1bHQ6IHN0cmluZztcclxuICBzdWNjZXNzOiBib29sZWFuO1xyXG59O1xyXG5cclxuLy8g2KrYp9io2Lkg2KfYsdiy24zYp9io24wg2LnYqNin2LHYp9iqINmF2YbYt9mC24xcclxuZnVuY3Rpb24gZXZhbHVhdGVMb2dpY2FsRXhwcmVzc2lvbihleHByZXNzaW9uOiBzdHJpbmcpOiBzdHJpbmcge1xyXG4gIC8vINit2LDZgSDZgdin2LXZhNmH4oCM2YfYp9uMINin2LbYp9mB24xcclxuICBjb25zdCBjbGVhbkV4cHJlc3Npb24gPSBleHByZXNzaW9uLnRyaW0oKS50b1VwcGVyQ2FzZSgpO1xyXG5cclxuICAvLyDYqNix2LHYs9uMINi52YXZhNqv2LHZh9inXHJcbiAgaWYgKGNsZWFuRXhwcmVzc2lvbi5pbmNsdWRlcygnQU5EJykpIHtcclxuICAgIGNvbnN0IHBhcnRzID0gY2xlYW5FeHByZXNzaW9uLnNwbGl0KCdBTkQnKS5tYXAocGFydCA9PiBwYXJ0LnRyaW0oKSk7XHJcbiAgICByZXR1cm4gYEFORCBvcGVyYXRpb24gd2l0aCBvcGVyYW5kczogJHtwYXJ0cy5qb2luKCcgYW5kICcpfWA7XHJcbiAgfSBlbHNlIGlmIChjbGVhbkV4cHJlc3Npb24uaW5jbHVkZXMoJ09SJykpIHtcclxuICAgIGNvbnN0IHBhcnRzID0gY2xlYW5FeHByZXNzaW9uLnNwbGl0KCdPUicpLm1hcChwYXJ0ID0+IHBhcnQudHJpbSgpKTtcclxuICAgIHJldHVybiBgT1Igb3BlcmF0aW9uIHdpdGggb3BlcmFuZHM6ICR7cGFydHMuam9pbignIG9yICcpfWA7XHJcbiAgfSBlbHNlIGlmIChjbGVhbkV4cHJlc3Npb24uaW5jbHVkZXMoJ05PVCcpKSB7XHJcbiAgICBjb25zdCBvcGVyYW5kID0gY2xlYW5FeHByZXNzaW9uLnJlcGxhY2UoJ05PVCcsICcnKS50cmltKCk7XHJcbiAgICByZXR1cm4gYE5PVCBvcGVyYXRpb24gb246ICR7b3BlcmFuZH1gO1xyXG4gIH1cclxuXHJcbiAgcmV0dXJuICdJbnZhbGlkIGV4cHJlc3Npb24gLSBwbGVhc2UgdXNlIEFORCwgT1IsIG9yIE5PVCBvcGVyYXRvcnMnO1xyXG59XHJcblxyXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBoYW5kbGVyKHJlcTogTmV4dEFwaVJlcXVlc3QsIHJlczogTmV4dEFwaVJlc3BvbnNlPERhdGE+KSB7XHJcbiAgdHJ5IHtcclxuICAgIGlmIChyZXEubWV0aG9kICE9PSAnUE9TVCcpIHtcclxuICAgICAgY29uc29sZS5sb2coJ0ludmFsaWQgbWV0aG9kOicsIHJlcS5tZXRob2QpO1xyXG4gICAgICByZXR1cm4gcmVzLnN0YXR1cyg0MDUpLmpzb24oeyByZXN1bHQ6ICdNZXRob2Qgbm90IGFsbG93ZWQnLCBzdWNjZXNzOiBmYWxzZSB9KTtcclxuICAgIH1cclxuXHJcbiAgICBjb25zdCB7IGV4cHJlc3Npb24gfSA9IHJlcS5ib2R5O1xyXG4gICAgY29uc29sZS5sb2coJ1JlY2VpdmVkIGV4cHJlc3Npb246JywgZXhwcmVzc2lvbik7XHJcblxyXG4gICAgaWYgKCFleHByZXNzaW9uIHx8IHR5cGVvZiBleHByZXNzaW9uICE9PSAnc3RyaW5nJykge1xyXG4gICAgICByZXR1cm4gcmVzLnN0YXR1cyg0MDApLmpzb24oe1xyXG4gICAgICAgIHJlc3VsdDogJ0ludmFsaWQgaW5wdXQgZXhwcmVzc2lvbicsXHJcbiAgICAgICAgc3VjY2VzczogZmFsc2VcclxuICAgICAgfSk7XHJcbiAgICB9XHJcblxyXG4gICAgLy8g2KfYsdiy24zYp9io24wg2LnYqNin2LHYqiDZhdmG2LfZgtuMXHJcbiAgICBjb25zdCByZXN1bHQgPSBldmFsdWF0ZUxvZ2ljYWxFeHByZXNzaW9uKGV4cHJlc3Npb24pO1xyXG4gICAgY29uc29sZS5sb2coJ0V2YWx1YXRpb24gcmVzdWx0OicsIHJlc3VsdCk7XHJcbiAgICBcclxuICAgIHJldHVybiByZXMuc3RhdHVzKDIwMCkuanNvbih7IFxyXG4gICAgICByZXN1bHQsXHJcbiAgICAgIHN1Y2Nlc3M6IHRydWUgXHJcbiAgICB9KTtcclxuXHJcbiAgfSBjYXRjaCAoZXJyb3IpIHtcclxuICAgIGNvbnNvbGUuZXJyb3IoJ0FQSSBFcnJvcjonLCBlcnJvcik7XHJcbiAgICByZXR1cm4gcmVzLnN0YXR1cyg1MDApLmpzb24oeyBcclxuICAgICAgcmVzdWx0OiAnU2VydmVyIGVycm9yJywgXHJcbiAgICAgIHN1Y2Nlc3M6IGZhbHNlIFxyXG4gICAgfSk7XHJcbiAgfVxyXG59Il0sIm5hbWVzIjpbImV2YWx1YXRlTG9naWNhbEV4cHJlc3Npb24iLCJleHByZXNzaW9uIiwiY2xlYW5FeHByZXNzaW9uIiwidHJpbSIsInRvVXBwZXJDYXNlIiwiaW5jbHVkZXMiLCJwYXJ0cyIsInNwbGl0IiwibWFwIiwicGFydCIsImpvaW4iLCJvcGVyYW5kIiwicmVwbGFjZSIsImhhbmRsZXIiLCJyZXEiLCJyZXMiLCJtZXRob2QiLCJjb25zb2xlIiwibG9nIiwic3RhdHVzIiwianNvbiIsInJlc3VsdCIsInN1Y2Nlc3MiLCJib2R5IiwiZXJyb3IiXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///(api)/./src/pages/api/infer.ts\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../webpack-api-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("(api)/./src/pages/api/infer.ts"));
module.exports = __webpack_exports__;

})();