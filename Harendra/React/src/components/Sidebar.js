import React from 'react';
import { Route, Link } from "react-router-dom";
import A from '../views/A/A';
import B from '../views/B/B';

function Sidebar() {
    return (
        <div className="row no-gutters">
            <div className="col-2 side-nav">
                <ul>
                    <li>
                        <Link to="/">
                            <div className="image-wrapper">
                                <img src={require('../images/side-nav/risk.jpg')} alt="sample"/>
                            </div>
                                Check Risk Rating 
                        </Link>
                    </li>

                    <li>
                        <Link to="/about">
                            <div className="image-wrapper">
                                <img src={require('../images/side-nav/customer.png')} alt="sample" />
                            </div>
                                View Customer Details
                        </Link>
                    </li>

                    <li>
                    <div className="image-wrapper">
                        <img src={require('../images/side-nav/searching.jpg')} alt="sample" />
                    </div>
                       Request a loan
                    </li>

                    <li>
                    <div className="image-wrapper">
                        <img src={require('../images/side-nav/loan.jpg')} alt="sample" />
                    </div>
                       Check Loan details
                    </li>

                    <li>
                    <div className="image-wrapper">
                        <img src={require('../images/side-nav/manager.jpg')} alt="sample" />
                    </div>
                        Contact Manager
                    </li>

                    <li>
                    <div className="image-wrapper">
                        <img src={require('../images/side-nav/error.jpg')} alt="sample" />
                    </div>
                        Report an error
                    </li>
                </ul>
            </div>
            <div className="col-10">
                <Route exact path="/" component={A}/>
                <Route path="/about" component={B} />
            </div>
        </div>
    )
}

export default Sidebar;