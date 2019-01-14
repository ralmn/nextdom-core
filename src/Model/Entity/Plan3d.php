<?php
/* This file is part of NextDom Software.
 *
 * NextDom is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NextDom Software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NextDom Software. If not, see <http://www.gnu.org/licenses/>.
 */

namespace NextDom\Model\Entity;

/**
 * Plan3d
 *
 * @ORM\Table(name="plan3d", indexes={@ORM\Index(name="name", columns={"name"}), @ORM\Index(name="link_type_link_id", columns={"link_type", "link_id"}), @ORM\Index(name="fk_plan3d_plan3dHeader1_idx", columns={"plan3dHeader_id"})})
 * @ORM\Entity
 */
class Plan3d
{

    /**
     * @var string
     *
     * @ORM\Column(name="name", type="string", length=255, nullable=true)
     */
    private $name;

    /**
     * @var string
     *
     * @ORM\Column(name="link_type", type="string", length=127, nullable=true)
     */
    private $linkType;

    /**
     * @var string
     *
     * @ORM\Column(name="link_id", type="string", length=127, nullable=true)
     */
    private $linkId;

    /**
     * @var string
     *
     * @ORM\Column(name="position", type="text", length=65535, nullable=true)
     */
    private $position;

    /**
     * @var string
     *
     * @ORM\Column(name="display", type="text", length=65535, nullable=true)
     */
    private $display;

    /**
     * @var string
     *
     * @ORM\Column(name="css", type="text", length=65535, nullable=true)
     */
    private $css;

    /**
     * @var string
     *
     * @ORM\Column(name="configuration", type="text", length=65535, nullable=true)
     */
    private $configuration;

    /**
     * @var integer
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="IDENTITY")
     */
    private $id;

    /**
     * @var \NextDom\Model\Entity\Plan3dheader
     *
     * @ORM\ManyToOne(targetEntity="NextDom\Model\Entity\Plan3dheader")
     * @ORM\JoinColumns({
     *   @ORM\JoinColumn(name="plan3dHeader_id", referencedColumnName="id")
     * })
     */
    private $plan3dheader;

    public function getName()
    {
        return $this->name;
    }

    public function getLinkType()
    {
        return $this->linkType;
    }

    public function getLinkId()
    {
        return $this->linkId;
    }

    public function getPosition()
    {
        return $this->position;
    }

    public function getDisplay()
    {
        return $this->display;
    }

    public function getCss()
    {
        return $this->css;
    }

    public function getConfiguration()
    {
        return $this->configuration;
    }

    public function getId()
    {
        return $this->id;
    }

    public function getPlan3dheader(): \NextDom\Model\Entity\Plan3dheader
    {
        return $this->plan3dheader;
    }

    public function setName($name)
    {
        $this->name = $name;
        return $this;
    }

    public function setLinkType($linkType)
    {
        $this->linkType = $linkType;
        return $this;
    }

    public function setLinkId($linkId)
    {
        $this->linkId = $linkId;
        return $this;
    }

    public function setPosition($position)
    {
        $this->position = $position;
        return $this;
    }

    public function setDisplay($display)
    {
        $this->display = $display;
        return $this;
    }

    public function setCss($css)
    {
        $this->css = $css;
        return $this;
    }

    public function setConfiguration($configuration)
    {
        $this->configuration = $configuration;
        return $this;
    }

    public function setId($id)
    {
        $this->id = $id;
        return $this;
    }

    public function setPlan3dheader(\NextDom\Model\Entity\Plan3dheader $plan3dheader)
    {
        $this->plan3dheader = $plan3dheader;
        return $this;
    }

}
