import React, {useState} from "react";
import axios from "axios";
import '../App.css';
import config from '../config.json';
import {Button, Col, Form, Input, Radio, Row, Table} from "antd";


export default function ApplicationForm() {
    const [form] = Form.useForm();
    const [isDisabled, setDisabled] = useState(false);
    const [user, setUser] = useState({
        businessName: '',
        email: '',
        estYear: '',
        empCount: '',
        accProvider: ''
    });
    const [balanceSheet, setBalanceSheet] = useState();
    const columns = [{
            title: 'Assets Value',
            dataIndex: 'assetsValue',
            key: 'assetsValue'
        },
        {
            title: 'Month',
            dataIndex: 'month',
            key: 'month'
        },
        {
            title: 'Profit Or Loss',
            dataIndex: 'profitOrLoss',
            key: 'profitOrLoss'
        },
        {
            title: 'Year',
            dataIndex: 'year',
            key: 'year'
        }
    ]

    // set user input in state
    const handleInput = name => e => {
        setUser({...user, [name]:e.target.value});
    };

    // get balance sheet from third party accounting services
    function getBalanceSheet() {
        setDisabled(true);
        let baseUrl = config.ACCOUNTING_SERVICE+config.GET_BALANCE_SHEET_EP;
        axios.post(baseUrl, JSON.stringify(user), {
            headers: {'Content-Type': 'application/json'}
        })
            .then((response)=>{
                setBalanceSheet(response.data.data.sheet)
                console.log(response.data.data.sheet)
            });
        console.log(user);
    }

    // clear fields and enable input form
    function resetForm() {
        setDisabled(false);
        setUser({
            businessName: '',
            email: '',
            estYear: '',
            empCount: '',
            accProvider: ''
        });
        form.resetFields();
        setBalanceSheet([])
    }

    // send loan application to backend
    function submitApplication() {
        console.log('In submit');
    }

    return (
        <div className={"form"}>
            <h1 className={"form-heading"}>New Application</h1>
            <div className={"form-business"}>
                <div className={"form-business-body"}>
                    <h4>BUSINESS DETAILS</h4>
                    <Form form={form} name={"basic"} layout={"vertical"} onFinish={getBalanceSheet}>
                        <Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
                            <Col xs={24} sm={24} md={12} lg={12} xl={12}>
                                <Form.Item label={"Name of Business"} name={"business-name"}
                                           rules={[{required:true, message:"Please enter business name"}]}>
                                    <Input onChange={handleInput('businessName')} disabled={isDisabled}/>
                                </Form.Item>
                            </Col>
                            <Col xs={24} sm={24} md={12} lg={12} xl={12}>
                                <Form.Item label={"Email"} name={"business-email"}
                                           rules={[{required:true, message:"Please enter the email address"}]}>
                                    <Input onChange={handleInput('email')} disabled={isDisabled}/>
                                </Form.Item>
                            </Col>
                            <Col xs={24} sm={24} md={12} lg={12} xl={12}>
                                <Form.Item label={"Established Year"} name={"business-year"}
                                           rules={[{required:true, message:"Please enter the established year"}]}>
                                    <Input onChange={handleInput('estYear')} disabled={isDisabled}/>
                                </Form.Item>
                            </Col>
                            <Col xs={24} sm={24} md={12} lg={12} xl={12}>
                                <Form.Item label={"No. of Employees"} name={"business-emp"}>
                                    <Input onChange={handleInput('empCount')} disabled={isDisabled}/>
                                </Form.Item>
                            </Col>
                        </Row>
                        <div className={"form-radio-group"}>
                            <h4>ACCOUNTING PROVIDER</h4>
                            <Form.Item label={"Select your accounting provider"} name={"acc-provider"}
                                           rules={[{required:true, message:"Please select your accounting provider"}]}>
                            <Radio.Group onChange={handleInput('accProvider')} disabled={isDisabled}>
                                <Radio value={"xero"}>XERO</Radio>
                                <Radio value={"myob"}>MYOB</Radio>
                            </Radio.Group>
                            </Form.Item>
                        </div>
                        <Button type={"primary"} htmlType={"submit"}>View Balance Sheet</Button>
                        <Button type={"default"} onClick={resetForm} className={"reset-btn"}>Reset Form</Button>
                        <Table className={"balance-table"} dataSource={balanceSheet}
                               columns={columns} rowKey={"month"}/>
                    </Form>
                    <Button type={"primary"} htmlType={"submit"}
                            className={"submit-btn"} disabled={!isDisabled}
                            onClick={submitApplication}>Submit Application</Button>
                </div>
            </div>
        </div>
    )
}