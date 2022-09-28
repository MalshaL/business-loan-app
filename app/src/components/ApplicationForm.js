import React from "react";
import '../App.css';
import {Button, Col, Form, Input, Radio, Row, Table} from "antd";


export default function ApplicationForm() {
    return (
        <div className={"form"}>
            <h1 className={"form-heading"}>New Application</h1>
            <div className={"form-business"}>
                <div className={"form-business-body"}>
                    <h4>BUSINESS DETAILS</h4>
                    <Form name={"basic"} layout={"vertical"}>
                        <Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
                            <Col xs={24} sm={24} md={12} lg={12} xl={12}>
                                <Form.Item label={"Name of Business"} name={"business-name"}
                                           rules={[{required:true, message:"Please enter business name"}]}>
                                    <Input/>
                                </Form.Item>
                            </Col>
                            <Col xs={24} sm={24} md={12} lg={12} xl={12}>
                                <Form.Item label={"Email"} name={"business-email"}
                                           rules={[{required:true, message:"Please enter the email address"}]}>
                                    <Input/>
                                </Form.Item>
                            </Col>
                            <Col xs={24} sm={24} md={12} lg={12} xl={12}>
                                <Form.Item label={"Established Year"} name={"business-year"}
                                           rules={[{required:true, message:"Please enter the established year"}]}>
                                    <Input/>
                                </Form.Item>
                            </Col>
                            <Col xs={24} sm={24} md={12} lg={12} xl={12}>
                                <Form.Item label={"No. of Employees"} name={"business-emp"}>
                                    <Input/>
                                </Form.Item>
                            </Col>
                        </Row>
                        <div className={"form-radio-group"}>
                            <h4>ACCOUNTING PROVIDER</h4>
                            <p>Select your accounting provider</p>
                            <Radio.Group>
                                <Radio value={"xero"}>XERO</Radio>
                                <Radio value={"myob"}>MYOB</Radio>
                            </Radio.Group>
                        </div>
                        <Button type={"primary"}>View Balance Sheet</Button>
                        <Table className={"balance-table"}/>
                        <Button type={"primary"} htmlType={"submit"} className={"submit-btn"}>Submit Application</Button>
                    </Form>
                </div>
            </div>
        </div>
    )
}