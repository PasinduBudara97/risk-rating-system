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
                                <img src={require('../images/side-nav/add_item.png')} alt="sample"/>
                            </div>
                                Add Item
                        </Link>
                    </li>

                    <li>
                        <Link to="/about">
                            <div className="image-wrapper">
                                <img src={require('../images/side-nav/borrow_item.png')} alt="sample" />
                            </div>
                                Borrow Item
                        </Link>
                    </li>

                    <li>
                    <div className="image-wrapper">
                        <img src={require('../images/side-nav/display_item.png')} alt="sample" />
                    </div>
                        Display Item
                    </li>

                    <li>
                    <div className="image-wrapper">
                        <img src={require('../images/side-nav/return_item.png')} alt="sample" />
                    </div>
                        Return Item
                    </li>

                    <li>
                    <div className="image-wrapper">
                        <img src={require('../images/side-nav/delete_item.png')} alt="sample" />
                    </div>
                        Delete Item
                    </li>

                    <li>
                    <div className="image-wrapper">
                        <img src={require('../images/side-nav/generate_report.png')} alt="sample" />
                    </div>
                        Generate Report
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